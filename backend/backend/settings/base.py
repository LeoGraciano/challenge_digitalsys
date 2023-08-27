from .middleware_settings import *  # noqa: ignore=F401 isort:skip
from .installed_apps_settings import *  # noqa: ignore=F401 isort:skip
from .internationalizations_settings import *  # noqa: ignore=F401 isort:skip
from .auth_settings import *  # noqa: ignore=F401 isort:skip
from .host_settings import *  # noqa: ignore=F401 isort:skip
from .media_settings import *  # noqa: ignore=F401 isort:skip
from .database_settings import *  # noqa: ignore=F401 isort:skip
from .celery_settings import *  # noqa: ignore=F401 isort:skip
from .rest_framework_settings import *  # noqa: ignore=F401 isort:skip

from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)

DJANGO_SETTINGS_MODULE = config("DJANGO_SETTINGS_MODULE")

ROOT_URLCONF = "backend.urls"

WSGI_APPLICATION = "backend.wsgi.application"

DEVELOPMENT = config("DEVELOPMENT", default=True, cast=bool)

if not DEVELOPMENT:
    print("DEVELOPMENT", DEVELOPMENT)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
