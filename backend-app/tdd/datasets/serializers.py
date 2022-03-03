from rest_framework import serializers
from .models import *



class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ('name', 'description')


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ('name', 'description')


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('name', 'description')


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ('name', 'description')


class CompressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compression
        fields = ('name', 'description')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'description')


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ('name', 'description')

class DatasetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataset
        fields = ('id', 'name', 'catalog', 'short_description')


class DatasetDetailSerializer(serializers.ModelSerializer):

    format = serializers.CharField(source='format.name', read_only=True)
    type = serializers.CharField(source='type.name', read_only=True)
    data_type = serializers.CharField(source='data_type.name', read_only=True)
    source = serializers.CharField(source='source.name', read_only=True)
    license = serializers.CharField(source='license.name', read_only=True)
    compression = serializers.CharField(source='compression.name', read_only=True)
    annotations = AnnotationSerializer(read_only=True, many=True)

    class Meta:
        model = Dataset
        fields = ('id', 'name', 'catalog', 'doi', 'short_description', 'description', 'version', 'format',
            'type', 'data_type', 'source', 'license', 'compression', 'annotations', 'download_size', 'authors', 'release_date')
