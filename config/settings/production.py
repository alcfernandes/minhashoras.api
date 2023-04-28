from .base import *  # noqa

# GENERAL
ALLOWED_HOSTS = env.list(
    'DJANGO_ALLOWED_HOSTS',
    default=[
        'minhashoras-api.fly.dev',
        'localhost',
        '127.0.0.1',
    ],
)
CSRF_TRUSTED_ORIGINS = env.list(
    'DJANGO_CSRF_TRUSTED_ORIGINS', default=['https://minhashoras-api.fly.dev']
)
