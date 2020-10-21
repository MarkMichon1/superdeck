from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from administrative.models import Address, City, Instance, State

admin.site.register(Address)
admin.site.register(City)
admin.site.register(Instance)
admin.site.register(State)
