from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'build/static',
]

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'build'],
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
