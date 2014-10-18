"""
Local development settings
"""

from timgorin.settings.base import *


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

INTERNAL_IPS = (
    '127.0.0.1',
)

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'assets', 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(REPOSITORY_ROOT, 'assets', 'media')

MEDIA_URL = '/media/'

# Local email server
# `python -m smtpd -n -c DebuggingServer localhost:1025`

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}
