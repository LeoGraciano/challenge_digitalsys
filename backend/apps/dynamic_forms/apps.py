from django.apps import AppConfig


class DynamicFormsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.dynamic_forms"

    def ready(self) -> None:
        import apps.dynamic_forms.signals  # noqa: F401

        return super().ready()
