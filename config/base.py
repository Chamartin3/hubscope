"""
Django settings for sisop project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

Project generated at: 2020-05-20T18:15:26.485237

"""

import os
import json

COMMON_FILE=open('config/commons.json','r')
VUE_CONFIG=json.load(COMMON_FILE)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ',_8S,6#JNfOfn==uBz(w!_T[(>TS1iOs}0P{uG/eNX};Ab1t=O'

# SECURITY WARNING: don't run with debug turned on in production!
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', False)
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MODULE_APPS = [
    'rest_framework',
    'drf_generators',
    'webpack_loader',
    'hubscope.vue_django',
]

MY_APPS = [
    'hubscope.accounts',
    'hubscope.reports',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hubscope.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['public'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'hubscope',
    #     'USER': 'root',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-VE'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = VUE_CONFIG['static_folder']


STATICFILES_DIRS = [
    os.path.join(BASE_DIR+VUE_CONFIG['static_folder']),
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME':  os.path.join(BASE_DIR+VUE_CONFIG['output']),
        'CACHE': not DEBUG,
        'TIMEOUT': None,
        'STATS_FILE': os.path.join(BASE_DIR+VUE_CONFIG['stats_file']),
    }
}

LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = 'dashboard'
AUTH_USER_MODEL = "accounts.User"

DJV_API_URLS='hubscope.api'
DLV_AUTH_PATH = "api/accounts/auth"


COMMON_FILE.close()
