from apps.accounts.manager import UserManager
from apps.core.models import BaseFields
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin, BaseFields):
    objects = UserManager()

    email = models.EmailField(_("E-mail"), unique=True, db_column="email")

    name = models.CharField(
        _("Nome completo"),
        max_length=100,
    )

    date_joined = models.DateTimeField(default=timezone.now)

    last_login = models.DateTimeField(default=timezone.now)
    is_trusty = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_username(self):
        return self.email

    def get_short_name(self):
        return self.name.split(" ")[0]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")
