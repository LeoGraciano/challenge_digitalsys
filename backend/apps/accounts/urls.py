from apps.accounts import views as v_accounts
from apps.accounts.api import viewsets as vs_accounts
from apps.accounts.api.viewsets import MyObtainTokenPairView
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()

router.register(r"detail", vs_accounts.UserDetail, basename="UserDetail")

router.register(r"token", vs_accounts.TokenDetail, basename="TokenDetail")

router.register(r"token-update", vs_accounts.TokenUpdate, basename="TokenUpdate")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("login-token/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", v_accounts.Login.as_view(), name="login"),
    path("logout/", v_accounts.Login.as_view(), name="logout"),
]

# AJAX
ajax_urls = [
    path("endpoint-auth-login/", v_accounts.ajax_login, name="json_auth_login"),
    path("endpoint-logout/", v_accounts.ajax_logout, name="json_logout"),
]

urlpatterns += ajax_urls
