from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class ExampleView(APIView):
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
    serializer_class = ForamtSerializer
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