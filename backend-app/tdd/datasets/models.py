import boto
from django.db import models
from tdd.models import BaseModel
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from datetime import date

from users.models import User
import uuid
from .config_aws import (
    AWS_UPLOAD_BUCKET,
    AWS_UPLOAD_REGION,
    AWS_UPLOAD_ACCESS_KEY_ID,
    AWS_UPLOAD_SECRET_KEY
)

class Enum(BaseModel):
    """This abstract model, will represent a dynamic enumeration that can be expanded in the future"""

    name = models.CharField(max_length=64, verbose_name=_("name"))
    description = models.CharField(max_length=250,blank=True,verbose_name=_("description"))

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CatalogEnum(Enum):
    """This abstract model, will have an additional field that have acronym to be encoded in the catalog number"""
    catalog_acronym = models.CharField(max_length=10, blank=False, verbose_name=_("catalog acronym"))

    class Meta:
        abstract = True


class DataType(Enum):
    """DataType represent the data type of the content of a dataset i.e. text, image, etc.."""
    pass


class Annotation(Enum):
    """Annotation stores the annotation type of a dataset i.e. raw-text, pos-tagged, etc.."""
    pass


class Source(Enum):
    """Source enumeration represent the genre of this dataset's source i.e. wiki, academic, books, etc.."""
    pass


class Format(Enum):
    """Format enumeration represent the format of this dataset's files i.e. txt, json, xml, etc.."""
    pass

class Compression(Enum):
    """Compression type of the dataset bundle"""
    pass


class Type(CatalogEnum):
    """Type represent the type of a dataset i.e. corpus, treebank etc.."""
    pass


class License(CatalogEnum):
    """License of the dataset, cc, bsd, mit etc.."""
    pass


class Dataset(BaseModel):
    """Dataset model will store the metafields of a dataset"""

    # required
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='ID')
    catalog = models.CharField(max_length=128, verbose_name=_("catalog"), unique=True)
    name = models.CharField(max_length=128, verbose_name=_("name"))
    short_description = models.TextField(max_length=512, blank=True, verbose_name=_("short description"))
    description = models.TextField(max_length=10000, blank=True, verbose_name=_("description"))
    is_visible = models.BooleanField(default=True)
    version = models.CharField(blank=False, max_length=10, verbose_name=_("version"), help_text="version of the dataset")

    # single required enums
    format = models.ForeignKey(Format, on_delete=models.CASCADE, verbose_name=_("format"))
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name=_("type"))
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE, verbose_name=_("data type"))
    source = models.ForeignKey(Source, on_delete=models.CASCADE, verbose_name=_("data source"))
    license = models.ForeignKey(License, on_delete=models.CASCADE, verbose_name=_("license"))
    compression = models.ForeignKey(Compression, on_delete=models.CASCADE, verbose_name=_("Compression"))

    # many to many enums
    annotations = models.ManyToManyField(Annotation, verbose_name=_("annotations"))

    # optional
    doi = models.URLField(blank=True)
    download_size = models.CharField(max_length=100,verbose_name=_("download size"))
    authors = models.CharField(max_length=256, verbose_name=_("authors"), help_text="comma seperated")
    release_date = models.DateField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding:
            serial_number = Dataset.objects.filter(create_date__date__month=date.today().month, type=self.type).count() + 1
            serial_number = "{0:0=3d}".format(serial_number)
            self.catalog = "TDD-" + self.type.catalog_acronym + "-" + str(date.today().year) + "{0:0=2d}".format(date.today().month) + "-" + self.license.catalog_acronym + "-" + serial_number

        return super(Dataset, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        fileItem = FileItem.objects.filter(dataset=self).first()
        fileItem.delete()
        return super(Dataset,self).delete(*args, **kwargs)


    class Meta:
        ordering = ['release_date']


class Download(BaseModel):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, verbose_name=_("format"))
    link_count = models.IntegerField( default=0, verbose_name=_("link count"))


class FileItem(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, verbose_name=_("dataset"))
    path = models.TextField(blank=True, null=True)
    size = models.BigIntegerField(default=0)
    file_type = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    @property
    def title(self):
        return str(self.name)

    def delete(self, *args, **kwargs):
        REGION_HOST = 's3.{}.amazonaws.com'.format(AWS_UPLOAD_REGION)
        conn = boto.connect_s3(AWS_UPLOAD_ACCESS_KEY_ID, AWS_UPLOAD_SECRET_KEY, host=REGION_HOST)
        bucket = conn.get_bucket(AWS_UPLOAD_BUCKET)
        for key in bucket.list(prefix=self.path):
            key.delete()
        return super(FileItem,self).delete(*args, **kwargs)
