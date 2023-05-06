from .base import *  # noqa

# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['debug_toolbar']  # noqa F405
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa F405
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']


# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions']  # noqa F405
SHELL_PLUS = 'ipython'
