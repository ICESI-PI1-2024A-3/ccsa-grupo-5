from django.apps import AppConfig


class PetitionConfig(AppConfig):
    """
    Configuration class for the petition app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petition'
