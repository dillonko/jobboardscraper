"""
Django settings for timgorin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

################################
### HEROKU-SPECIFIC SETTINGS ###
################################

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(SETTINGS_DIR, os.pardir)
REPOSITORY_DIR = os.path.join(BASE_DIR, os.pardir)


# Website settings

SECRET_KEY = os.environ.get('TIMGORIN_SECRET_KEY')

DEBUG = os.environ.get('DEBUG', True)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'easy_timezones',
    'pure_pagination',
    'widget_tweaks',
    'haystack',
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
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'easy_timezones.middleware.EasyTimezoneMiddleware',
)

ROOT_URLCONF = 'timgorin.urls'

WSGI_APPLICATION = 'timgorin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_ROOT = os.path.join(REPOSITORY_DIR, 'assets', 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Media
# https://docs.djangoproject.com/en/1.7/topics/files/

MEDIA_ROOT = os.path.join(REPOSITORY_DIR, 'assets', 'media')

MEDIA_URL = '/media/'


# Templates
# https://docs.djangoproject.com/en/1.7/ref/templates/

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'timgorin.context_processors.search_form',
)


# Other settings

SITE_ID = 1

REMOVE_WWW = True

INTERNAL_IPS = (
    '127.0.0.1',
)

PAGINATE_BY = 25

GEOIP_DATABASE = os.path.join(SETTINGS_DIR, 'GeoLiteCity.dat')


# Pagination

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 2,
    'MARGIN_PAGES_DISPLAYED': 1,
}


# Haystack

from urlparse import urlparse

es = urlparse(os.environ.get('SEARCHBOX_URL', 'http://127.0.0.1:9200/'))

port = es.port or 80

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': '%s://%s:%s' % (es.scheme, es.hostname, port),
        'INDEX_NAME': 'haystack',
    },
}

if es.username:
    HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": es.username + ':' + es.password}


################################
### HEROKU-SPECIFIC SETTINGS ###
################################

# https://devcenter.heroku.com/articles/getting-started-with-django

ALLOWED_HOSTS += [
    '.herokuapp.com'
]

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config(
    default='sqlite:///{}'.format(DATABASES['default']['NAME'])
)

# Enable Connection Pooling for PostgreSQL (if desired)
if DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
    DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Static asset configuration
STATIC_ROOT = 'staticfiles'

# Simplified static file serving.
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Other security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
