from datetime import timedelta

import environ
from decouple import config

from minhashoras_apps import __api_version__ as api_version

ROOT_DIR = (
    environ.Path(__file__) - 3
)  # (minhashoras-api/config/settings/base.py - 3 = minhashoras-api/)


# BASIC SETTINGS
# ------------------------------------------------------------------------------
SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# APPLICATIONS SETTINGS
# ------------------------------------------------------------------------------
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'rest_framework_simplejwt',
    'corsheaders',
    'auditlog',
    'storages',
    'minhashoras_apps.accounts.apps.AccountsConfig',
]

# MIDDLEWARE AND URL CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# TEMPLATE SETTINGS
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# DATABASE SETTINGS
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT'),
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# INTERNATIONALIZATION SETTINGS
# ------------------------------------------------------------------------------
LANGUAGE_CODE = config('LANGUAGE_CODE', default='pt-br')
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [ROOT_DIR.path('locale')]

# STATIC FILES AND MEDIA SETTINGS
# ------------------------------------------------------------------------------
APPS_DIR = ROOT_DIR.path('minhashoras_apps')
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATICFILES_DIRS = [str(APPS_DIR.path('static'))]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

USE_S3 = config('USE_S3', default=False, cast=bool)
if USE_S3:
    # STORAGES
    # ------------------------
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_QUERYSTRING_AUTH = False

    _AWS_EXPIRY = (
        60 * 60 * 24 * 7
    )  # DO NOT change these unless you know what you're doing.
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': f'max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate'
    }
    AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default=None)
    AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN', default=None)
    aws_s3_domain = (
        AWS_S3_CUSTOM_DOMAIN or f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    )

    # STATIC
    # ------------------------
    STATICFILES_STORAGE = (
        'minhashoras_apps.utils.storages.StaticRootS3Boto3Storage'
    )
    COLLECTFAST_STRATEGY = 'collectfast.strategies.boto3.Boto3Strategy'
    STATIC_URL = f'https://{aws_s3_domain}/static/'

    # MEDIA
    # ------------------------
    DEFAULT_FILE_STORAGE = (
        'minhas_horas_apps.utils.storages.MediaRootS3Boto3Storage'
    )
    MEDIA_URL = f'https://{aws_s3_domain}/media/'
else:
    STATIC_URL = '/django_static/'
    MEDIA_URL = '/django_media/'

# AUTHENTICATION AND SECURITY SETTINGS
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = 'accounts.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')

CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS', default='http://localhost:3000'
).split(',')

# DJANGO REST FRAMEWORK SETTINGS
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# SIMPLE JWT SETTINGS
# ------------------------------------------------------------------------------
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# CORS SETTINGS
# ------------------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS', default='http://localhost:3000'
).split(',')
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_CREDENTIALS = True

# SWAGGER (SPECTACULAR) SETTINGS
# ------------------------------------------------------------------------------
SPECTACULAR_SETTINGS = {
    'TITLE': 'MinhasHoras API',
    'DESCRIPTION': 'Time tracking application',
    'VERSION': api_version,
    'SERVE_INCLUDE_SCHEMA': False,
    'SCHEMA_PATH_PREFIX': r'/api/',
}

# AUDITLOG SETTINGS
# ------------------------------------------------------------------------------
AUDITLOG_INCLUDE_ALL_MODELS = True

# LOGGING SETTINGS
# ------------------------------------------------------------------------------
LOG_LEVEL = config('DJANGO_LOG_LEVEL', default='INFO')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
            '%(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'root': {'level': LOG_LEVEL, 'handlers': ['console']},
}

# DJANGO ADMIN INTERFACE SETTINGS
# ------------------------------------------------------------------------------
X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']
