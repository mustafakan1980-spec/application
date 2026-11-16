"""
Django settings for Application project.
"""
import os
from pathlib import Path
import dj_database_url
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / '.env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    if os.getenv('DEBUG', 'False').lower() in ('true', '1', 't'):
        SECRET_KEY = 'django-insecure-dev-fallback-key-replace-in-production'
    else:
        raise ImproperlyConfigured("SECRET_KEY ortam değişkeni ayarlanmalıdır.")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

# Hosts
allowed_hosts_raw = os.getenv('ALLOWED_HOSTS', '')
if allowed_hosts_raw:
    ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_raw.split(',') if host.strip()]
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

if '.vercel.app' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('.vercel.app')

if DEBUG and '*' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('*')

# CSRF Trusted Origins
csrf_trusted_raw = os.getenv('CSRF_TRUSTED_ORIGINS', '')
if csrf_trusted_raw:
    CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in csrf_trusted_raw.split(',') if origin.strip()]
else:
    CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000', 'http://[::1]:8000']

if 'https://*.vercel.app' not in CSRF_TRUSTED_ORIGINS:
    CSRF_TRUSTED_ORIGINS.append('https://*.vercel.app')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # Local apps
    'accounts.apps.AccountsConfig',
    'catalog.apps.CatalogConfig',
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# SQLite fallback KOYMA; DATABASE_URL zorunlu (Supabase PostgreSQL)
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ImproperlyConfigured(
        "\n========================================================================\n"
        "HATA: DATABASE_URL ortam değişkeni bulunamadı!\n"
        "Bu proje Supabase PostgreSQL bağlantısı ile çalışır. SQLite fallback kullanılmaz.\n"
        "Lütfen .env dosyanızı oluşturup geçerli bir DATABASE_URL ekleyin.\n"
        "Örnek: DATABASE_URL=postgresql://postgres:[ŞİFRE]@db.[REF].supabase.co:5432/postgres\n"
        "========================================================================\n"
    )

DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=0,  # Supabase transaction pooler uyumu için
        disable_server_side_cursors=True,  # Supabase transaction pooler (port 6543) uyumu
    )
}

# Custom User Model
AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = [
    'accounts.authentication.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'tr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('tr', 'Türkçe'),
    ('en', 'English'),
    ('fr', 'Français'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# Supabase Storage & Client Settings
SUPABASE_URL = os.getenv('SUPABASE_URL', '')
SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY', '')
SUPABASE_SERVICE_ROLE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY', '')
SUPABASE_STORAGE_BUCKET = os.getenv('SUPABASE_STORAGE_BUCKET', 'sample-documents')

# Auth Redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------------------
# Production Security Settings (FAZ 6)
# -----------------------------------------------------------------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'True').lower() == 'true'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = int(os.getenv('SECURE_HSTS_SECONDS', '31536000'))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
else:
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

