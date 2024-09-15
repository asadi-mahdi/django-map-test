"""
Django settings for my_test_project project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oruze(j-**(msr!#_dmtwikdldrxel9+thu^&!vcinyr!tq3l7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_gis',
    # 'rest_framework.authtoken',
    'members',
    'gisapp',
    'django.contrib.gis',
    'corsheaders',
    'oauth2_provider',
]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ]
# }
# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER': 'test_map_github.my_test_project.my_test_project.exceptions.custom_exception_handler'
# }


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# }

# OAUTH2_PROVIDER = {
#     'RESOURCE_SERVER_INTROSPECTION_URL': 'http://127.0.0.1:8001/o/introspect/',
#     'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': ('LTVlrvajsEOzVVVrxqkhhce11fjM2kVJlj2Da2AS',
#                                                   'UUTqouJeY2EhvLcVUWOn7TIS0yth26OTr5r5IzrYbjaxSpKRfzjwgSiwHmMSMM9Ma74lRmeoU7cqkTIyKRWtsBdp02RPwa9qmIp8mAW7AKhDM6kotBMncdTqNZCVRMmL'),
# }
# OAUTH2_PROVIDER = {
#     # 'OIDC_ENABLED': True,
#     # 'OIDC_ISS_ENDPOINT': 'http://172.16.11.24:8080/sso/oauth2',
#
#     'RESOURCE_SERVER_INTROSPECTION_URL': 'http://172.16.11.24:8080/sso/oauth2/introspect',
#     'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': ('ssoClient-2',
#                                                   'ssoClientSecret-2'),
# }

# AUTHENTICATION_BACKENDS = (
#     # 'django.contrib.auth.backends.ModelBackend',
#     'oauth2_provider.backends.OAuth2Backend',
# )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # custom middleware for authorization
    # 'test_map_github.my_test_project.my_test_project.middleware.SimpleMiddleware',
    # 'oauth2_provider.middleware.OAuth2TokenMiddleware',
    # middleware for translation according to LANGUAGE_CODE
    'django.middleware.locale.LocaleMiddleware',
    'test_map_github.my_test_project.my_test_project.middleware.ExceptionMiddleware',
]

ROOT_URLCONF = 'my_test_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_test_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mresalat_test',
        'USER': 'postgres',
        'PASSWORD': 'Ictdb19',
        'HOST': '172.16.11.19',
        'PORT': '5432',
        'TIME_ZONE': 'Asia/Tehran'
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

# LOCALE_PATHS = [
#     "test_map_github/my_test_project/my_test_project/locale",
# ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    "C:\\Users\\dev25\\Desktop\\Django\\django-test\\my_test_project\\my_test_project\\static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ERRORS_PATH = "\\mapdata\\runtimeexception"

LOGIN_REDIRECT_URL = "/gisapp/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

# CORS_ALLOWED_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://localhost:3000$",
]
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

GDAL_LIBRARY_PATH = "C:\\Users\\dev25\\Desktop\\Django\\tessst_github\\django-map-test\\venv\\Lib\\site-packages\\osgeo\\gdal.dll"
# GDAL_LIBRARY_PATH = "D:\\python\\django-map-test\\venv\\Lib\\site-packages\\osgeo\\gdal.dll"
GEOS_LIBRARY_PATH = "C:\\Users\\dev25\\Desktop\\Django\\tessst_github\\django-map-test\\venv\\Lib\\site-packages\\osgeo\\geos_c.dll"
# GEOS_LIBRARY_PATH = "D:\\python\\django-map-test\\venv\\Lib\\site-packages\\osgeo\\geos_c.dll"

os.environ[
    'PROJ_LIB'] = "C:\\Users\\dev25\\Desktop\\Django\\tessst_github\\django-map-test\\venv\\Lib\\site-packages\\osgeo\\data\\proj"
# os.environ['PROJ_LIB'] = "D:\\python\\django-map-test\\venv\\Lib\\site-packages\\osgeo\\data\\proj"
