# """Development settings."""

from .base import *  # NOQA
from .base import env, env_aux

# Base
DEBUG = True

# Security


ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

RENDER_EXTERNAL_HOSTNAME = env_aux.get('RENDER_EXTERNAL_HOSTNAME', None)

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
#     'http://127.0.0.1:3000',
#     'http://localhost:3001',
#     'http://localhost:3002',
#     'http://localhost:3003',
#     'http://localhost:3005',
#     'http://localhost:8001',
# ]


CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:3001',
    'http://localhost:3002',
    'http://localhost:3003',
    'http://localhost:3005',
    'http://localhost:8001',
]


RENDER_EXTERNAL_HOSTNAME = env_aux.get('RENDER_EXTERNAL_HOSTNAME', '')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS += [RENDER_EXTERNAL_HOSTNAME]
    CORS_ALLOWED_ORIGINS += [RENDER_EXTERNAL_HOSTNAME]
    CORS_ALLOWED_ORIGINS += [f'{RENDER_EXTERNAL_HOSTNAME}:3000']
    # CORS_ORIGIN_WHITELIST += [RENDER_EXTERNAL_HOSTNAME]
    # CORS_ORIGIN_WHITELIST += [f'{RENDER_EXTERNAL_HOSTNAME}:3000']

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# Email
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# django-extensions
# INSTALLED_APPS += ['django_extensions']  # noqa F405
