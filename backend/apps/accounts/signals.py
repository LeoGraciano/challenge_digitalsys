from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_delete, sender=Token)
def delete_auth_token(sender, instance, **kwargs):
    if User.objects.filter(pk=instance.user.pk).exists():
        Token.objects.create(user=instance.user)
