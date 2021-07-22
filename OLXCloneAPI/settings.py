"""
Django settings for OLXCloneAPI project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from decouple import config
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cf778$q46ya=q3k5ll5k2&$l$(_0^===_&^n7*syos&32zh)n#'

# SECURITY WARNING: don't run with debug turned on in production!
if config("DJANGO_DEVELOPEMT") == "true":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # core
    'account.apps.AccountConfig',
    'ad.apps.AdConfig',
    'category.apps.CategoryConfig',

    # third party
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist'

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OLXCloneAPI.urls'
AUTH_USER_MODEL = 'account.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'OLXCloneAPI.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DATABASE_NAME'),
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASSWORD'),
            'HOST': config('DATABASE_HOST'),
            'PORT': config('DATABASE_PORT'),
            'OPTIONS': {'sslmode': config('SSL_REQUIRE')}
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# AWS_ACCESS_KEY_ID = 'MR6HZXYRJ4TBSBGC2A4B'
# AWS_SECRET_ACCESS_KEY = 'x5Sfmqeurb2PDjq86VTUN9cqsWn5sgmHvbGY2XLpQbg'
# AWS_STORAGE_BUCKET_NAME = 'flashapp'
# AWS_S3_REGION_NAME = 'ap-south-1'
# AWS_S3_ENDPOINT_URL = 'https://sgp1.digitaloceanspaces.com'
# AWS_S3_CUSTOM_DOMAIN = 'd1xurv31sxeawq.cloudfront.net'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'flashmedia'
# AWS_DEFAULT_ACL = 'public-read'
#
# DEFAULT_FILE_STORAGE = 'flashAPI.custom_storages.CustomS3Boto3Storage'
# MEDIA_URL = '%s/%s/media/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

X_FRAME_OPTIONS = 'ALLOWALL'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 6d828rd8b2&hu#$^5464
# SIMPLE JWT

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(minutes=15),
    'UPDATE_LAST_LOGIN': True,
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken', 'rest_framework_simplejwt.tokens.RefreshToken',),
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'PREPEND_MEDIA_URL': True,

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',

    # THROTTLING
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/day',  # throttle for non-loggedin users
        'user': '100/min'  # throttle for loggedin users
    }

}


# gmail_send/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nixcircle@gmail.com'
EMAIL_HOST_PASSWORD = 'bxzgzkqrtpdenmzu'  # past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS = True


"""
#Endpoints

::Accounts
- Login
- Login via google
- Get User

::Ads
- Create Ad
- Delete Ad
- Get Ads
    - Search by name
    - Filter by category
    - Filter by location
    - My Ads
    - My Fav Ads
- Make ad favourite
- Get Ad

::Category
- Get categories

"""
