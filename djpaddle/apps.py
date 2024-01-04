from django.apps import AppConfig
from . import settings

class DjpaddleConfig(AppConfig):
    """
    Configuration for the djpaddle Django application.
    """

    name = "djpaddle"
    default_auto_field = settings.DJPADDLE_DEFAULT_AUTO_FIELD or "django.db.models.AutoField"
