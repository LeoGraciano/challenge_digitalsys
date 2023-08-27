from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# route = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("api-auth/", include("rest_framework.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
