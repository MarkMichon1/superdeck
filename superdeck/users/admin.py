from django.contrib import admin

from users.models import AppUser, ClientData, EmployeeData


admin.site.register(AppUser)
admin.site.register(ClientData)
admin.site.register(EmployeeData)