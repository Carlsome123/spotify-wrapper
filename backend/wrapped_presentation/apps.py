from django.apps import AppConfig


class WrappedPresentationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "wrapped_presentation"