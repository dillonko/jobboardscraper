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

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
# MEDIA_ROOT = ''
# MEDIA_URL = ''

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'https://4ayozlr:h5ww2lmryzca7iqz@holly-2519000.us-east-1.bonsai.io:443/',
        'INDEX_NAME': 'haystack',
    },
}
