import os
from pathlib import Path
from decouple import config

# ================= BASE =================
BASE_DIR = Path(__file__).resolve().parent.parent

# ================= SECURITY =================
SECRET_KEY = config(
    'SECRET_KEY',
    default='django-insecure-k9$##c5#jg7z&1yq=4r1a(f5e-v#we&4ekh0lcmoa)dp7z)=97'
)

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',
    'muhammadalii.uz',
    'www.muhammadalii.uz',
]

# ================= INSTALLED APPS =================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_pages',
]

# ================= MIDDLEWARE =================
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

# ================= URLS / WSGI =================
ROOT_URLCONF = 'Conf.urls'

WSGI_APPLICATION = 'Conf.wsgi.application'

# ================= TEMPLATES =================
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
            ],
        },
    },
]

# ================= DATABASE =================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ================= PASSWORD VALIDATORS =================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================= LANGUAGE / TIME =================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# ================= STATIC FILES =================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise (ENG MUHIM QISM)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = ['.map']

# ================= MEDIA =================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ================= OTHER =================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
RESUME_PATH = 'resume/'

# ================= RECAPTCHA =================
RECAPTCHA_PUBLIC_KEY = "6LfzCygsAAAAAKns4sIp-FebWZpD7ZuDvUjXzvWt"
RECAPTCHA_SECRET_KEY = "6LfzCygsAAAAANMlWytBGCNUxZ-cceSf3n3b1h8c"
