from .base import *

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		'NAME': os.getenv('DATABASE_NAME', 'postgres'),
		'USER': os.getenv('DATABASE_USERNAME', 'postgres'),
		'PASSWORD': os.getenv('DATABASE_PASSWORD', 'postgres'),
		'HOST': os.getenv('DATABASE_HOST', 'db'),
		'PORT': os.getenv('DATABASE_PORT', 5432),
	}
}

INTERNAL_IPS = ["localhost", "127.0.0.1"]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
	{ "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
	{ "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
	{ "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
	{ "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = BASE_DIR / "static/"
