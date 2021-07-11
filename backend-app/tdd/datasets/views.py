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
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from aws_request_signer import AwsRequestSigner

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
        queryset = Dataset.objects.filter(is_visible=True)

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
        user = request.user
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
                    dataset_id = request.data.get("dataset")
            )
        _, file_extension = os.path.splitext(filename_req)

        if filename_req and file_extension:
            """
            Save the eventual path to the Django-stored FileItem instance
            """
            file_obj.path = upload_start_path
            file_obj.save()

        url = 'https://{bucket}.s3-{region}.amazonaws.com/'.format(
                        bucket=AWS_UPLOAD_BUCKET,
                        region=AWS_UPLOAD_REGION
                        )
        data = {
            "url": url + upload_start_path,
            "filename": filename_req,
            "file_id": file_obj_id
        }
        return Response(data, status=status.HTTP_200_OK)

class FileItemHeaders(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request_signer = AwsRequestSigner(
            AWS_UPLOAD_REGION, AWS_UPLOAD_ACCESS_KEY_ID, AWS_UPLOAD_SECRET_KEY, "s3"
        )
        # upload_file = request.FILES['data']
        upload_hash = request.data.get('hash')
        url = request.data.get('url')
        # content_hash = hashlib.sha256(upload_file.read()).hexdigest()
        headers = {"Content-Type": "*"}
        headers.update(
            request_signer.sign_with_headers("PUT", url, headers, upload_hash)
        )
        return Response(headers, status=status.HTTP_200_OK)

@method_decorator(login_required(login_url='/admin/'), name='dispatch')
class FileUploadView(TemplateView):
    template_name = "upload.html"

    def get_context_data(self, **kwargs):
        context = super(FileUploadView, self).get_context_data(**kwargs)
        dataset = kwargs.get("id", None)
        token, created = Token.objects.get_or_create(user=self.request.user)
        context['dataset'] = str(dataset) if dataset else None
        context['token'] = str(token.key)
        return context


class FileUploadCompleteHandler(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
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

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        fileItem = FileItem.objects.get(dataset_id=request.data.get("dataset"))
        REGION_HOST = 's3.{}.amazonaws.com'.format(AWS_UPLOAD_REGION)
        conn = boto.connect_s3(AWS_UPLOAD_ACCESS_KEY_ID, AWS_UPLOAD_SECRET_KEY, host=REGION_HOST)
        bucket = conn.get_bucket(AWS_UPLOAD_BUCKET)
        s3_file_path = bucket.get_key(fileItem.path + '/' + fileItem.name)
        url = s3_file_path.generate_url(expires_in=60) # expiry time is in seconds
        download, created = Download.objects.get_or_create(dataset_id=request.data.get("dataset"))
        download.link_count += 1
        download.save() 
        return JsonResponse({"url": url},safe=False)  


def delete_file(request, id):
    fileItem = FileItem.objects.get(dataset_id=id)
    fileItem.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
