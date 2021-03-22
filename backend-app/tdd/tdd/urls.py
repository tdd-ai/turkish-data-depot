"""tdd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, re_path, include
from django.conf import settings

import django_cas_ng.views
from .views import ApplicationView, favicon_view

urlpatterns = [
	re_path(r"^$", ApplicationView.as_view(), name="Application"),
	path('admin/', admin.site.urls),
	path('favicon.ico', favicon_view),
    path('accounts/login', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('accounts/logout', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
]

from datasets.urls import datasets_router, datasets_urlpatterns

urlpatterns += datasets_router.urls
urlpatterns += datasets_urlpatterns

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "Turkish Data Depot"