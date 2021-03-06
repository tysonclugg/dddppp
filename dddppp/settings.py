"""
Django settings for dddppp project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import pkg_resources
import pwd

PROJECT_NAME = 'dddppp'

# Enforce a valid POSIX environment
# Get missing environment variables via call to pwd.getpwuid(...)
_PW_CACHE = None
_PW_MAP = {
    'LOGNAME': 'pw_name',
    'USER': 'pw_name',
    'USERNAME': 'pw_name',
    'UID': 'pw_uid',
    'GID': 'pw_gid',
    'HOME': 'pw_dir',
    'SHELL': 'pw_shell',
}
for _missing_env in set(_PW_MAP).difference(os.environ):
    if _PW_CACHE is None:
        _PW_CACHE = pwd.getpwuid(os.getuid())
    os.environ[_missing_env] = str(getattr(_PW_CACHE, _PW_MAP[_missing_env]))
del _PW_CACHE, _PW_MAP, pwd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nfd_lvt=&k#h#$a^_l09j#5%s=mg+0aw=@t84ry$&rps43c33+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dddp',
    'dddp.server',
    'dddp.accounts',
    'dddppp.slides',
]

for (requirement, pth) in [
    ('django-extensions', 'django_extensions'),
]:
    try:
        pkg_resources.get_distribution(requirement)
    except (
        pkg_resources.DistributionNotFound,
        pkg_resources.VersionConflict,
    ):
        continue
    INSTALLED_APPS.append(pth)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'dddppp.urls'

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

WSGI_APPLICATION = 'dddppp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PGDATABASE', PROJECT_NAME),
        'USER': os.environ.get('PGUSER', os.environ['LOGNAME']),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('PGHOST', ''),
        'PORT': os.environ.get('PGPORT', ''),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-au'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# django-secure
# see: https://github.com/carljm/django-secure/ for more options
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_FRAME_DENY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

DDDPPP_CONTENT_TYPES = []
PROJ_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
