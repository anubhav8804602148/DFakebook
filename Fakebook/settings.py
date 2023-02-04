from pathlib import Path
import mimetypes

mimetypes.add_type("text/javascript", ".js", True)
mimetypes.add_type("text/html", ".html", True)
mimetypes.add_type("text/css", ".css", True)
BASE_DIR = Path(__file__).resolve().parent.parent
LOGIN_REDIRECT_URL = '/application/all_apps'
LOGOUT_REDIRECT_URL = '/login'
SECRET_KEY = 'django-insecure-xue!ug6u5(3@w-_s@=n+0eqqy%uka=8zuy$*pp91ow$btr6nt2'
DEBUG = False

ALLOWED_HOSTS = [
    "*"
]

INSTALLED_APPS = [
    'Fakebook',
    'ManageApplications',
    'ProfileManagement',
    'ChatBox',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Fakebook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
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

WSGI_APPLICATION = 'Fakebook.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Fakebook',
        'USER': 'anubhav',
        'PASSWORD': 'anubhav',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'fakebook.log'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False,
        },
        'fakebook': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': False
        },
    },
}

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ('static',)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 3600
