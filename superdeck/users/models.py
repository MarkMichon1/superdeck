from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models


class AppUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        pass


class EmployeeData(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)


class ClientData(models.Model):
    pass


class Address(models.Model):
    pass