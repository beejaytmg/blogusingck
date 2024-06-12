import os
from pathlib import Path
import dj_database_url

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key and debug settings
SECRET_KEY = 'your-secret-key'
DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = [
    'blogusingck-production.up.railway.app',
    '127.0.0.1',
    'localhost',
    'bijayakumartamang.com.np'
]

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'ckeditor_uploader',
    'blogapp',
    'ckeditor',
]
CSRF_TRUSTED_ORIGINS = [
    'https://blogusingck-production.up.railway.app',
    'https://bijayakumartamang.com.np',
]
ALLOWED_HOSTS = [
    'blogusingck-production.up.railway.app',
    '127.0.0.1',
    'localhost',
    'bijayakumartamang.com.np'
]
# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'blogproject.urls'

# Templates
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

# WSGI application
WSGI_APPLICATION = 'blogproject.wsgi.application'

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:pLEeRpmrcKdSZFqrsPrjNVIcsLhNXQuW@roundhouse.proxy.rlwy.net:53242/railway'
    )
}

# Password validation
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

# CKEditor configuration
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' 
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': 'auto',
        'extraPlugins': ','.join([
            'codesnippet',
            'uploadimage',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
        ]),
    },
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
CKEDITOR_UPLOAD_PATH = 'uploads/ckeditor/'

# Static files directories
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
