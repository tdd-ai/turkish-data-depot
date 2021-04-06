from rest_framework import serializers
from .models import *


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('name',)

class DatasetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataset
        fields = ('name', 'catalog', 'short_description')


class DatasetDetailSerializer(serializers.ModelSerializer):

    format = serializers.CharField(source='foramt.name', read_only=True)
    type = serializers.CharField(source='type.name', read_only=True)
    data_type = serializers.CharField(source='data_type.name', read_only=True)
    source = serializers.CharField(source='source.name', read_only=True)
    license = serializers.CharField(source='license.name', read_only=True)
    annotations = AnnotationSerializer(read_only=True, many=True)

    class Meta:
        model = Dataset
        fields = ('name', 'catalog', 'short_description', 'description', 'version', 'format',
            'type', 'data_type', 'source', 'license', 'annotations', 'download_size', 'authors', 'release_date')