from apps.dynamic_forms.models import CreditAnalysisFields
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=CreditAnalysisFields)
def cred_form_unique_active(sender, instance, created, **kwargs):
    if instance.is_active:
        CreditAnalysisFields.objects.exclude(pk=instance.pk).update(is_active=False)
