import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Website settings

SECRET_KEY = os.environ.get('SECRET_KEY', 'knv3mcls)af%i!m2(8byle2#%=qa6#^)!h=@#nvs)nc*g)a7u4')

DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.herokuapp.com'
]

INTERNAL_IPS = (
    '127.0.0.1',
)


# Application definition

INSTALLED_APPS = [
    # Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Third-party
    'debug_toolbar',
    'easy_timezones',
    'pure_pagination',
    'widget_tweaks',
    'haystack',

    # Project
    'jobs',
    'organizations',
    'search',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'easy_timezones.middleware.EasyTimezoneMiddleware',
]

ROOT_URLCONF = 'jobboardscraper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'jobboardscraper.context_processors.search_form',
            ],
        },
    },
]

WSGI_APPLICATION = 'jobboardscraper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir, 'static')),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media
# https://docs.djangoproject.com/en/1.10/topics/files/

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'assets', 'media')

MEDIA_URL = '/media/'


# Sites
# https://docs.djangoproject.com/en/1.10/ref/contrib/sites/

SITE_ID = 1


# Heroku
# https://devcenter.heroku.com/articles/getting-started-with-django

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Haystack
# http://django-haystack.readthedocs.io/en/v2.5.0/
# https://devcenter.heroku.com/articles/searchbox#using-haystack-with-django

from urllib.parse import urlparse

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


# django-pure-pagination
# https://github.com/jamespacileo/django-pure-pagination

PAGINATE_BY = 20

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 2,
    'MARGIN_PAGES_DISPLAYED': 1,
}


# django-easy-timezones
# https://github.com/Miserlou/django-easy-timezones

GEOIP_DATABASE = os.path.join(PROJECT_ROOT, 'GeoLiteCity.dat')

GEOIPV6_DATABASE = os.path.join(PROJECT_ROOT, 'GeoLiteCityv6.dat')


# Other settings

REMOVE_WWW = True
