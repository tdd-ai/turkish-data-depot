# settings for development
from .base import *

DEBUG = True

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
	BASE_DIR / "static/"
]

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]


INTERNAL_IPS = ["localhost", "127.0.0.1"]
ALLOWED_HOSTS = ["*"]


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []
