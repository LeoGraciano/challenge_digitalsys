from apps.core.models import BaseFields
from django.db import models
from django.utils.translation import gettext_lazy as _


class CreditAnalysisFields(BaseFields):
    name = models.CharField(_("Formulário"), max_length=50, unique=True)
    field_data = models.JSONField(_("Campos"), null=True, default=dict)

    is_active = models.BooleanField(_("Ativo"), default=False)

    def get_fields(self):
        return self.field_data

    class Meta:
        db_table = "tb_credit_analysis_fields"
        verbose_name = _("Formulário de analise de credito")
        verbose_name_plural = _("Formulários de analise de credito")
