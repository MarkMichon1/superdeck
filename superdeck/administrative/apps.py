from django.apps import AppConfig
from django.db.utils import ProgrammingError


class AdministrativeConfig(AppConfig):
    name = 'administrative'

    def ready(self):
        try:
            from administrative.utilities import cache_initialize, database_initialization_check
            database_initialization_check()
            cache_initialize()
        except ProgrammingError:
            pass