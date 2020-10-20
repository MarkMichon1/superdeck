from django.apps import AppConfig


class AdministrativeConfig(AppConfig):
    name = 'administrative'

    def ready(self):
        from administrative.utilities import run_once_on_startup
        run_once_on_startup()