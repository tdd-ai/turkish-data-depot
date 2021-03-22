from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers
from .apis import *
from .views import *

datasets_router = routers.DefaultRouter()

datasets_urlpatterns = [
    path("api/example/", ExampleView.as_view(), name="example"),
    # re_path(r"^receive-message",ReceiveMessage.as_view(), name="receive"),
    # re_path(r"^send-message",SendMessage.as_view(), name="send"),
    # re_path(r"^send-trigger",SendTrigger.as_view(), name="trigger"),
    # re_path(r"^receive-message",ReceiveMessage.as_view(), name="receive"),
    # re_path(r"^trigger-scenario",TriggerScenarioManully.as_view(), name="receive"),
    # re_path(r"^send-receive",SendAndReceive.as_view(), name="send_receive"),
    # re_path(r"^similarity-check",SimilarityCheck.as_view(), name="similarity")
]