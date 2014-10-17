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



ES_URL = os.environ.get('BONSAI_URL')
 
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': ES_URL.scheme + '://' + ES_URL.hostname + ':80',
        'INDEX_NAME': 'haystack',
    },
}
 
if ES_URL.username:
    HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": ES_URL.username + ':' + ES_URL.password}
