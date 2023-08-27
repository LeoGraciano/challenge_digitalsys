from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from apps.core.utils.api.mixin import ListDestroyMixer, ListUpdateMixer
from apps.core.utils.api.permissions import IsAdminOrSelfObject, IsAdminOrIsRelatedUserObject
from apps.accounts.api import serializers as s_accounts
from apps.accounts import models as m_accounts
from rest_framework.authtoken.models import Token

from apps.core.utils.validator.str_regex import ValidationRegex


class UserDetail(ListUpdateMixer):

    serializer_class = s_accounts.UserSerializer
    queryset = m_accounts.User.objects.all()
    permission_classes = [IsAdminOrSelfObject]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        if not self.request.user.is_superuser:
            qs = qs.filter(pk=self.request.user.pk)

        return qs

    lookup_field = 'email'
    lookup_value_regex = ValidationRegex().regex_code_email()


class TokenDetail(viewsets.ReadOnlyModelViewSet):

    serializer_class = s_accounts.TokenSerializer
    queryset = Token.objects.all()
    permission_classes = [IsAdminOrIsRelatedUserObject]

    lookup_field = 'user__email'
    # E-mails is valid
    lookup_value_regex = ValidationRegex().regex_code_email()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        if not self.request.user.is_superuser:
            qs = qs.filter(user=self.request.user)

        return qs


class TokenUpdate(ListDestroyMixer):

    serializer_class = s_accounts.TokenSerializer
    queryset = Token.objects.all()
    permission_classes = [IsAdminOrIsRelatedUserObject]

    lookup_field = 'user__email'
    # E-mails is valid
    lookup_value_regex = ValidationRegex().regex_code_email()

    def get_queryset(self, *args, **kwargs):
        qs = self.queryset.filter(user=self.request.user)
        qs.delete()
        qs = Token.objects.filter(user=self.request.user)
        return qs


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = s_accounts.MyTokenObtainPairSerializer
