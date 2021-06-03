from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers
from .views import *

datasets_router = routers.DefaultRouter()

datasets_router.register('api/datasets', DatasetViewSet, basename='datasets')
datasets_router.register('api/enum/data-types', DataTypeViewSet)
datasets_router.register('api/enum/annotations', AnnotationViewSet)
datasets_router.register('api/enum/sources', SourceViewSet)
datasets_router.register('api/enum/formats', FormatViewSet)
datasets_router.register('api/enum/compressions', CompressionViewSet)
datasets_router.register('api/enum/types', TypeViewSet)
datasets_router.register('api/enum/licenses', LicenseViewSet)


datasets_urlpatterns = [
    path("api/example", ExampleView.as_view(), name="example"),
    url(r'^api/files/policy/$', FilePolicyAPI.as_view(), name='upload-policy'),
    url(r'^api/files/headers/$', FileItemHeaders.as_view(), name='file-headers'),
    url(r'^api/files/complete/$', FileUploadCompleteHandler.as_view(), name='upload-complete'),
    url(r'^upload/(?P<id>[^/]+)/$', FileUploadView.as_view(), name='upload-home'),
    url(r'^api/files/download/$', DownloadFile.as_view(), name="download-file")
]