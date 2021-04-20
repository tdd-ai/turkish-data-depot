import base64
import hashlib
import hmac
import os
import time
import boto
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

from .config_aws import (
    AWS_UPLOAD_BUCKET,
    AWS_UPLOAD_REGION,
    AWS_UPLOAD_ACCESS_KEY_ID,
    AWS_UPLOAD_SECRET_KEY
)


class ExampleView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': request.user.id,  # `django.contrib.auth.User` instance.
            "some": "response"
        }
        return Response(content)


class DataTypeViewSet(viewsets.ModelViewSet):
    serializer_class = DataTypeSerializer
    queryset = DataType.objects.all()
    http_method_names = ['get']


class AnnotationViewSet(viewsets.ModelViewSet):
    serializer_class = AnnotationSerializer
    queryset = Annotation.objects.all()
    http_method_names = ['get']


class SourceViewSet(viewsets.ModelViewSet):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()
    http_method_names = ['get']


class FormatViewSet(viewsets.ModelViewSet):
    serializer_class = FormatSerializer
    queryset = Format.objects.all()
    http_method_names = ['get']


class CompressionViewSet(viewsets.ModelViewSet):
    serializer_class = CompressionSerializer
    queryset = Compression.objects.all()
    http_method_names = ['get']


class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    http_method_names = ['get']


class LicenseViewSet(viewsets.ModelViewSet):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()
    http_method_names = ['get']


class DatasetViewSet(viewsets.ModelViewSet):
    serializer_class = DatasetDetailSerializer

    def get_queryset(self):
        queryset = Dataset.objects.all()

        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        formats = self.request.query_params.get('formats')
        if formats is not None:
            formats = formats.split(',')
            formats = Format.objects.filter(name__in=formats)
            queryset = queryset.filter(format__in=formats)

        types = self.request.query_params.get('types')
        if types is not None:
            types = types.split(',')
            types = Type.objects.filter(name__in=types)
            queryset = queryset.filter(type__in=types)

        data_types = self.request.query_params.get('data-types')
        if data_types is not None:
            data_types = data_types.split(',')
            data_types = DataType.objects.filter(name__in=data_types)
            queryset = queryset.filter(data_type__in=data_types)

        sources = self.request.query_params.get('sources')
        if sources is not None:
            sources = sources.split(',')
            sources = Source.objects.filter(name__in=sources)
            queryset = queryset.filter(source__in=sources)

        licenses = self.request.query_params.get('licenses')
        if licenses is not None:
            licenses = licenses.split(',')
            licenses = License.objects.filter(name__in=licenses)
            queryset = queryset.filter(license__in=licenses)

        compressions = self.request.query_params.get('compressions')
        if compressions is not None:
            compressions = compressions.split(',')
            compressions = Compression.objects.filter(name__in=compressions)
            queryset = queryset.filter(compression__in=compressions)

        annotations = self.request.query_params.get('annotations')
        if annotations is not None:
            annotations = annotations.split(',')
            annotations = Annotation.objects.filter(name__in=annotations)
            queryset = queryset.filter(annotations__in=annotations)

        return queryset

    def list(self, request):
        self.queryset = self.get_queryset()
        serializer = DatasetListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class FilePolicyAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """
    This view is to get the AWS Upload Policy for our s3 bucket.
    What we do here is first create a FileItem object instance in our
    Django backend. This is to include the FileItem instance in the path
    we will use within our bucket as you'll see below.
    """

    def post(self, request, *args, **kwargs):
        """
        The initial post request includes the filename
        and auth credientails. In our case, we'll use
        Session Authentication but any auth should work.
        """
        filename_req = request.data.get('filename')
        if not filename_req:
                return Response({"message": "A filename is required"}, status=status.HTTP_400_BAD_REQUEST)
        policy_expires = int(time.time()+5000)
        user = request.user
        username_str = str(request.user.first_name)
        """
        Below we create the Django object. We'll use this
        in our upload path to AWS.

        Example:
        To-be-uploaded file's name: Some Random File.mp4
        Eventual Path on S3: <bucket>/username/2312/2312.mp4
        """
        file_obj = FileItem.objects.create(user=user, name=filename_req, dataset_id=request.data.get("dataset"))
        
        file_obj_id = file_obj.id
        upload_start_path = "{dataset_id}/".format(
                    username = username_str,
                    dataset_id = request.data.get("dataset")
            )
        _, file_extension = os.path.splitext(filename_req)
        """
        Eventual file_upload_path includes the renamed file to the
        Django-stored FileItem instance ID. Renaming the file is
        done to prevent issues with user generated formatted names.
        """

        if filename_req and file_extension:
            """
            Save the eventual path to the Django-stored FileItem instance
            """
            file_obj.path = upload_start_path
            file_obj.save()

        policy_document_context = {
            "expire": policy_expires,
            "bucket_name": AWS_UPLOAD_BUCKET,
            "key_name": "",
            "acl_name": "private",
            "content_name": "",
            "content_length": 524288000,
            "upload_start_path": upload_start_path,

            }
        policy_document = """
        {"expiration": "2019-01-01T00:00:00Z",
          "conditions": [
            {"bucket": "%(bucket_name)s"},
            ["starts-with", "$key", "%(upload_start_path)s"],
            {"acl": "%(acl_name)s"},

            ["starts-with", "$Content-Type", "%(content_name)s"],
            ["starts-with", "$filename", ""],
            ["content-length-range", 0, %(content_length)d]
          ]
        }
        """ % policy_document_context
        aws_secret = str.encode(AWS_UPLOAD_SECRET_KEY)
        policy_document_str_encoded = str.encode(policy_document.replace(" ", ""))
        url = 'https://{bucket}.s3-{region}.amazonaws.com/'.format(
                        bucket=AWS_UPLOAD_BUCKET,
                        region=AWS_UPLOAD_REGION
                        )
        policy = base64.b64encode(policy_document_str_encoded)
        signature = base64.b64encode(hmac.new(aws_secret, policy, hashlib.sha1).digest())
        data = {
            "policy": policy,
            "signature": signature,
            "key": AWS_UPLOAD_ACCESS_KEY_ID,
            "file_bucket_path": upload_start_path,
            "file_id": file_obj_id,
            "filename": filename_req,
            "url": url,
            "username": username_str,
        }
        return Response(data, status=status.HTTP_200_OK)

@method_decorator(login_required(login_url='/admin/'), name='dispatch')
class FileUploadView(TemplateView):
    template_name = "upload.html"

    def get_context_data(self, **kwargs):
        context = super(FileUploadView, self).get_context_data(**kwargs)
        dataset = kwargs.get("id", None)
        token, created = Token.objects.get_or_create(user=self.request.user)
        print(token.key)
        context['dataset'] = str(dataset) if dataset else None
        context['token'] = str(token.key)
        return context


class FileUploadCompleteHandler(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        file_id = request.POST.get('file')
        size = request.POST.get('fileSize')
        data = {}
        type_ = request.POST.get('fileType')
        if file_id:
            obj = FileItem.objects.get(id=int(file_id))
            obj.size = int(size)
            obj.uploaded = True
            obj.type = type_
            obj.save()
            data['id'] = obj.id
            data['saved'] = True
        return Response(data, status=status.HTTP_200_OK)


class DownloadFile(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        fileItem = FileItem.objects.get(dataset_id=request.data.get("dataset"))
        conn = boto.connect_s3(AWS_UPLOAD_ACCESS_KEY_ID, AWS_UPLOAD_SECRET_KEY)
        bucket = conn.get_bucket(AWS_UPLOAD_BUCKET)
        s3_file_path = bucket.get_key(FileItem.path)
        url = s3_file_path.generate_url(expires_in=60) # expiry time is in seconds
        download, created = Download.objects.get_or_create(dataset_id=request.data.get("dataset"))
        download.link_count += 1
        download.save() 
        return JsonResponse({"url": url},safe=False)  
