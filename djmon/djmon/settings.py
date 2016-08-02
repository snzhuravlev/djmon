"""
Django settings for djmon project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e(m%w(5n-26_!nqipj8_xe6!fzfr&u*k+@mvc9i2_-$ov2fqko'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'start',
    'monitora',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'djmon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'templates'),
#)

WSGI_APPLICATION = 'djmon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE':   'django.db.backends.oracle',
    'NAME': 'ols',
    'USER': 'djmon',
    'HOST': '10.1.8.171',
    'PORT': '1521',
    'PASSWORD': 'XSW123edc',
    'OPTIONS': {
        'threaded': True,
         },
    },
    'erc': {
    'ENGINE':   'django.db.backends.oracle',
    'NAME': 'erc',
    'USER': 'srg',
    'HOST': '10.1.8.7',
    'PORT': '1521',
    'PASSWORD': 'XSW123edc',
    'OPTIONS': {
        'threaded': True,
         },
    },
    'vp': {
    'ENGINE':   'django.db.backends.oracle',
    'NAME': 'vp',
    'USER': 'srg',
    'HOST': '10.1.8.8',
    'PORT': '1521',
    'PASSWORD': 'XSW123edc',
    'OPTIONS': {
        'threaded': True,
         },
    },
    'jp': {
    'ENGINE':   'django.db.backends.oracle',
    'NAME': 'jp',
    'USER': 'srg',
    'HOST': '10.1.8.9',
    'PORT': '1521',
    'PASSWORD': 'XSW123edc',
    'OPTIONS': {
        'threaded': True,
         },
    },
    'hope': {
    'ENGINE':   'django.db.backends.oracle',
    'NAME': 'hope',
    'USER': 'srg',
    'HOST': '10.1.8.10',
    'PORT': '1521',
    'PASSWORD': 'XSW123edc',
    'OPTIONS': {
        'threaded': True,
        },
     },
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
