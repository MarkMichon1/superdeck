from django.core.cache import cache
from django.db.utils import ProgrammingError

from administrative.models import Instance, State


def database_initialization_check():
    """Executed the first time the app runs post migration."""

    instance = Instance.load()

    if not instance.is_initialized:

        # Generating available states
        states = (('Alabama', 'AL'), ('Alaska', 'AK'), ('Arizona', 'AZ'), ('Arkansas', 'AR'), ('California', 'CA'),
                 ('Colorado', 'CO'), ('Connecticut', 'CT'), ('Delaware', 'DE'), ('Florida', 'FL'), ('Georgia', 'GA'),
                 ('Hawaii', 'HI'), ('Idaho', 'ID'), ('Illinois', 'IL'), ('Indiana', 'IN'), ('Iowa', 'IA'),
                 ('Kansas', 'KS'), ('Kentucky', 'KY'), ('Louisiana', 'LA'), ('Maine', 'ME'), ('Maryland', 'MD'),
                 ('Massachusetts', 'MA'), ('Michigan', 'MI'), ('Minnesota', 'MN'), ('Mississippi', 'MS'),
                 ('Missouri', 'MO'), ('Montana', 'MT'), ('Nebraska', 'NE'), ('Nevada', 'NV'), ('New Hampshire', 'NH'),
                 ('New Jersey', 'NJ'), ('New Mexico', 'NM'), ('New York', 'NY'), ('North Carolina', 'NC'),
                 ('North Dakota', 'ND'), ('Ohio', 'OH'), ('Oklahoma', 'OK'), ('Oregon', 'OR'), ('Pennsylvania', 'PA'),
                 ('Rhode Island', 'RI'), ('South Carolina', 'SC'), ('South Dakota', 'SD'), ('Tennessee', 'TN'),
                 ('Texas', 'TX'), ('Utah', 'UT'), ('Vermont', 'VT'), ('Virginia', 'VA'), ('Washington', 'WA'),
                 ('West Virginia', 'WV'), ('Wisconsin', 'WI'), ('Wyoming', 'WY'))

        for state in states:
            new_state = State(name=state[0], abbreviation=state[1])
            new_state.save()

        # Populating app with sample data
        # to do

        instance.is_initialized = True
        instance.save()

def cache_initialize():
    """Loads weather data into cache at startup.  May do more in future."""
    cache.delete_many(['instance.is_opened', 'instance.opening_time, instance.closing_time', 'email.24h_count'])
    instance = Instance.load()

    cache.set_many([])

    # Get count of number of emails