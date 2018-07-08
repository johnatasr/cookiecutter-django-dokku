"""
Django settings for {{cookiecutter.app_name}} project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import dj_database_url

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY',
                    default='zs$zd9my5&ob&v56s=!3s1#rbk(%rajxbkrjtbsz1+&)9*k-7b')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS',
                       default='localhost',)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    {%- if cookiecutter.use_rest_framework == "y" %}
    'rest_framework',
    {% endif %}

    {%- if cookiecutter.use_sentry == "y" %}
    # sentry
    'raven.contrib.django.raven_compat',
    {% endif %}

    {%- if cookiecutter.email_user == "y" %}
    '{{cookiecutter.app_name}}.users',
    {% endif %}
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

ROOT_URLCONF = '{{cookiecutter.app_name}}.urls'

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

WSGI_APPLICATION = '{{cookiecutter.app_name}}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DEFAULT_DATABASE = config('DATABASE_URL',
                          default='postgres://cramstack:cramstack@localhost:5432/cramstack',
                          cast=dj_database_url.parse)

DATABASES = {
    'default': DEFAULT_DATABASE
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

{%- if cookiecutter.use_celery == "y" %}
# Celery settings
CELERY_BROKER_URL = config('REDIS_URL', default='redis://localhost:6379')
{% endif %}

{%- if cookiecutter.email_user == "y" %}
AUTH_USER_MODEL = 'users.User'

# Config to make the registration email only
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
{% endif %}

{%- if cookiecutter.use_sentry == "y" %}
# Sentry configuration
RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN_URL', default=None),
}
{% endif %}