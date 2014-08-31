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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'assets', 'static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(REPOSITORY_ROOT, 'assets', 'media')

MEDIA_URL = '/media/'

# Local email server
# `python -m smtpd -n -c DebuggingServer localhost:1025`

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
