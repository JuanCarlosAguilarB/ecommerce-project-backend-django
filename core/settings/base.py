from pathlib import Path
import datetime
import os
import environ
import psycopg2.extensions
from corsheaders.defaults import default_headers
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

# https://stackoverflow.com/questions/75939945/im-facing-this-error-importerror-cannot-import-name-smart-text-from-django#:~:text=1%20Answer&text=This%20error%20is%20caused%20by,encoding%20in%20Django%204.0.
import django
from django.utils.encoding import smart_str
django.utils.encoding.smart_text = smart_str

# instanciamos objeto para lectura de variables de entorno
env = environ.Env()
env_aux = os.environ
environ.Env.read_env()


# nos aseguramos de la lectura de variables de entorno
ENVIRONMENT = env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='PB3aGvTmCkzaLGRAxDc3aMayKTPTDd5usT8gw4pCmKOk5AlJjh12pTrnNgQyOHCH')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

if DEBUG:
    ALLOWED_HOSTS = ['*',]
else:
    ALLOWED_HOSTS = []

# Application definition

DJANGO_APPS = [
    # 'daphne', # is a HTTP, HTTP2 and WebSocket protocol
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


THIRD_APPS = [
    'channels',
    'rest_framework_simplejwt',
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'drf_yasg',  # swagger
    # 'storages',
    'rest_framework.authtoken',
    'social.apps.django_app.default',
    'social_django',
    'django_filters',
    'silk',
    'django_extensions',  # for django shell_plus
    'django_jenkins',
]

# Obtiene la ruta completa de la carpeta "apps"
apps_dir = os.path.join(BASE_DIR.parent, 'apps')

# Obtiene una lista de nombres de las aplicaciones dentro de la carpeta "apps"
PROJECT_APPS = [f"apps.{name}" for name in os.listdir(
    apps_dir) if os.path.isdir(os.path.join(apps_dir, name))]

# PROJECT_APPS = []

# add user model custom
AUTH_USER_MODEL = "user.User"

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + PROJECT_APPS

# configuracion ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'autoParagraph': False
    }
}
CKEDITOR_UPLOAD_PATH = "/media/"


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'silk.middleware.SilkyMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}

# deafault database wiht sqlite3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://54.175.59.91:8001',
    'http://54.175.59.91'
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://54.175.59.91:8001',
    'http://54.175.59.91'
]

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

# protección extra a la base de datos
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/static')
]


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.AdminRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}


# Django Rest Framework JWT
# https://jpadilla.github.io/django-rest-framework-jwt/

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=31),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
}

FILE_UPLOAD_PERMISSIONS = 0o640


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# configuración para aws
if not DEBUG:
    DEFAULT_FROM_EMAIL = "Uridium <mail@uridium.network>"
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_USE_TLS = env('EMAIL_USE_TLS')

    # django-ckeditor will not work with S3 through django-storages without this line in settings.py
    AWS_QUERYSTRING_AUTH = False

    # aws settings
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = 'public-read'

    # s3 static settings

    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    # s3 public media settings

    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'core.storage_backends.MediaStore'


# django channels settings
ASGI_APPLICATION = 'core.asgi.application'

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {'hosts': [('localhost', 6379)]},
#     },
# }


# Jenkis settings
JENKINS_TASKS = (
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    # 'django_jenkins.tasks.run_jslint',
    'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_sloccount'
)


# django redis config
REDIS_HOST = os.environ.get(
    'REDIS_HOST', 'redis-10999.c15.us-east-1-4.ec2.cloud.redislabs.com')
REDIS_PORT = os.environ.get('REDIS_PORT', 10999)
REDIS_DB = os.environ.get('REDIS_DB', 0)
REDIS_PASSWORD = os.environ.get(
    'REDIS_PASSWORD', 'FCzBTUDMQw2O5Oc3wEHFSiaqKKBAsKUd')


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': REDIS_HOST,
        # password redis
        'OPTIONS': {
            'DB': REDIS_DB,
            'PASSWORD': os.environ.get('REDIS_PASSWORD', ''),
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
        # 'OPTIONS': {
        #     'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        # },
        'KEY_PREFIX': 'django_cache',
        "TIMEOUT": 60 * 15,  # in seconds: 60 * 15 (15 minutes)

    },
}

print(REDIS_HOST)

# test if coneccion to redis is ok
# from django.core.exceptions import ImproperlyConfigured
# import redis
# try:
#     # Configuración de conexión a Redis
#     redis_connection = redis.StrictRedis.from_url(
#         os.environ.get('REDIS_URL', 'localhost:6379'))

#     # Realiza una operación simple, por ejemplo, obtener la clave 'test'
#     redis_connection.set('test', 'exitooooooo')
#     test_value = redis_connection.get('test')

#     # Imprime un mensaje si la conexión y la operación fueron exitosas
#     print("Conexión exitosa a Redis. Valor de prueba:", test_value)
# except redis.exceptions.ConnectionError:
#     # Maneja la excepción de conexión a Redis
#     raise ImproperlyConfigured(
#         "No se pudo conectar a Redis. Verifica la configuración.")
# except Exception as e:
#     # Maneja otras excepciones que puedan surgir
#     raise ImproperlyConfigured(f"Error al conectar a Redis: {e}")


# celery settings
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Celery Configuration Options
CELERY_TIMEZONE = "Australia/Tasmania"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'projects.devs101@gmail.com'
EMAIL_HOST_PASSWORD = 'jbyvshlhqkmkqnpi'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
