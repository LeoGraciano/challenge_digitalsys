from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseFields(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)

    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    class Meta:
        abstract = True
