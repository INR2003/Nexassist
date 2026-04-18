from pathlib import Path
import os

# Base directory for the project (backend/)
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from backend/.env when present
try:
    from dotenv import load_dotenv
    load_dotenv(BASE_DIR / '.env')
except Exception:
    pass

SECRET_KEY = 'replace-this-with-a-secure-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
}

# Point to project URL configuration
ROOT_URLCONF = 'config.urls'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Frontend build directory
FRONTEND_DIR = BASE_DIR.parent / 'frontend' / 'dist'

# Serve frontend static assets (JS, CSS, images)
STATICFILES_DIRS = [
    FRONTEND_DIR / 'assets',
    FRONTEND_DIR / 'images',
]

# Minimal templates configuration required by Django admin
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', FRONTEND_DIR],
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

# PostgreSQL configuration (reads from env or backend/.env)
DB_NAME = os.getenv('DB_NAME', 'NEXA')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}