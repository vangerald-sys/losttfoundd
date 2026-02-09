"""
Django settings for lostandfound_project project.
Updated for Render Deployment: Static handling removed & Template paths fixed.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# --------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# SECURITY SETTINGS
# --------------------------------------------------
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-for-local-dev')

# DEBUG is True to show error details. Set to False for final launch.
DEBUG = True 

ALLOWED_HOSTS = ['losttfoundd-r41v.onrender.com', 'localhost', '127.0.0.1']

# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
INSTALLED_APPS = [
    'core',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    'crispy_forms',
    'crispy_tailwind',
    'widget_tweaks',
]

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------------------------------
# URL CONFIG
# --------------------------------------------------
ROOT_URLCONF = 'lostandfound_project.urls'

# --------------------------------------------------
# TEMPLATES (The fix for TemplateDoesNotExist)
# --------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # This tells Django to look in the /templates folder in your root directory
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

# --------------------------------------------------
# DATABASE
# --------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# STATIC & MEDIA FILES (Simplified to remove W004 warning)
# --------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# We removed STATICFILES_DIRS to stop the "Directory does not exist" warning.
# Django will now only look for static files inside your app folders or admin.
STATICFILES_DIRS = []

# WhiteNoise: Using a simpler storage to prevent errors if CSS is missing
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --------------------------------------------------
# AUTH SETTINGS
# --------------------------------------------------
LOGIN_URL = 'core:login'
LOGIN_REDIRECT_URL = 'core:dashboard'
LOGOUT_REDIRECT_URL = 'core:home'

# --------------------------------------------------
# EMAIL SETTINGS
# --------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'geraldcudia19@gmail.com' 
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD', 'dqzpdnqcyxftvzxz').strip()
DEFAULT_FROM_EMAIL = 'FOUND.IT SYSTEMS <geraldcudia19@gmail.com>'

# --------------------------------------------------
# CRISPY FORMS CONFIGURATION
# --------------------------------------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
