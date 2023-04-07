from .base import *  # noqa

# GENERAL
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])
