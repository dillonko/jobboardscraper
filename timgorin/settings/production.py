"""
Production settings
"""

from timgorin.settings.base import *


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'timgorin.herokuapp.com',
    '*'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
# MEDIA_ROOT = ''
# MEDIA_URL = ''


# Heroku configuration

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
