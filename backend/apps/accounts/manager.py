from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **kwargs):
        now = timezone.now()
        if not email:
            raise ValueError(_("Um email válido deve ser informado."))

        email = self.normalize_email(email)

        name = kwargs.get("name")
        if not name:
            raise ValidationError("name deve ser informado")

        user = self.model(
            name=name,
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **kwargs):
        return self._create_user(email, password, False, False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        user = self._create_user(email, password, True, True, **kwargs)
        user.is_active = True
        user.save(using=self._db)
        return user
