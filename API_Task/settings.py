"""
Django settings for API_Task project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import environ

##################################################
# FILE SYSTEM PATHS
##################################################
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
##################################################
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
##################################################

# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

env = environ.Env(
    SECRET_KEY=(str, "th15$i5$aN$uNsAfE+S3cr3t$k3y"),
    DEBUG=(bool, False),
)
environ.Env.read_env(BASE_DIR + '/.env')

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

##################################################
# DEPLOY SETTINGS
##################################################

ALLOWED_HOSTS = [
    '127.0.0.1',
    '.pythonanywhere.com'
]

WSGI_APPLICATION = 'API_Task.wsgi.application'

##################################################
# APPLICATION DEVELOPMENT
##################################################

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

USER_APPS = [
    'momo',
]

INSTALLED_APPS = DJANGO_APPS + USER_APPS

##################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

##################################################

ROOT_URLCONF = 'API_Task.urls'

##################################################
# FRONT END SETTINGS
##################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

##################################################
# DATABASE SETTINGS
##################################################
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

##################################################
# AUTHENTICATION SETTINGS
##################################################

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length':8}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = '/momo/user_login'
LOGOUT_REDIRECT_URL = ''

##################################################
# ASSETS SETTINGS
##################################################
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

##################################################
# INTERNATIONALIZATION SETTINGS
##################################################
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_L10N = True
USE_TZ = True
