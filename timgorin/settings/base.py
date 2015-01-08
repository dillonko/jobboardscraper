"""
Django settings for timgorin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = BASE_DIR
REPOSITORY_ROOT = os.path.join(PROJECT_ROOT, os.pardir)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'haystack',
    'easy_timezones',
    'jobs',
    'organizations',
    'search',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'easy_timezones.middleware.EasyTimezoneMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'timgorin.urls'

WSGI_APPLICATION = 'timgorin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'timgorin',
        'USER': 'timgorin',
        'PASSWORD': 'timgorin',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Templates

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'timgorin.context_processors.site',
    'timgorin.context_processors.search_form',
)

TEMPLATE_DIRS = (
    os.path.join(REPOSITORY_ROOT, 'templates'),
)


# Static

STATICFILES_DIRS = (
    os.path.join(REPOSITORY_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Website settings

SECRET_KEY = os.environ.get('TIMGORIN_SECRET_KEY')

SITE_ID = 1

PAGINATE_BY = 25

GEOIP_DATABASE = os.path.join(PROJECT_ROOT, 'GeoLiteCity.dat')
