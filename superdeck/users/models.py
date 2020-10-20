from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    name = models.CharField(max_length=14, unique=True)
    abbreviation = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return f'{self.abbreviation} -- {self.name}'


class City(models.Model):
    name = models.CharField(max_length=40)
    state = models.ForeignKey(State, null=True, related_name='cities', on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} -- {self.state.name}'


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    optional_line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    zip_code = models.IntegerField()
    state = models.Choices


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, password, **extra_fields)


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        pass #todo


class EmployeeData(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='employee_data')


class ClientData(models.Model):
    starred = models.BooleanField(default=False)