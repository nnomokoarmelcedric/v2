from django.apps import AppConfig


class RequetesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Requetes'

    def ready(self):
        from Requetes import signals