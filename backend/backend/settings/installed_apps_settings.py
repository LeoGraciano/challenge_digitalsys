BUSINESS_APPS = [
    "apps.core",
    "apps.accounts",
    "apps.dynamic_forms",
]

THIRD_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "celery",
    "django_celery_results",
    "django_celery_beat",
    "django_extensions",
    "django_filters",
    "corsheaders",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + BUSINESS_APPS
