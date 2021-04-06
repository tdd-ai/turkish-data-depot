from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers
from .views import *

datasets_router = routers.DefaultRouter()

datasets_router.register('api/datasets', DatasetViewSet)


datasets_urlpatterns = [
    path("api/example", ExampleView.as_view(), name="example"),
]