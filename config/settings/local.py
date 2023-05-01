from .base import *  # noqa

# GENERAL
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

# Cross-origin requests config
CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',
]
