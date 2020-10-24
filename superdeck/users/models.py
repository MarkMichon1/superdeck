from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


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
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('user_type', 'A')

        return self._create_user(email, password, **extra_fields)



class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    CLIENT = 'C'
    TECHNICIAN = 'T'
    RECEPTIONIST = 'R'
    MANAGER = 'M'
    ADMINISTRATOR = 'A'
    USER_TYPE_CHOICES = [
        (CLIENT, 'Client'),
        (TECHNICIAN, 'Technician'),
        (RECEPTIONIST, 'Receptionist'),
        (MANAGER, 'Manager'),
        (ADMINISTRATOR, 'Administrator'),
    ]

    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=CLIENT)

    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_user_type_humanize(self):

        label_dict = {'C': 'Client', 'T': 'Technician', 'R': 'Receptionist', 'M': 'Manager', 'A': 'Administrator'}
        return label_dict[self.user_type]

    class Meta:
        verbose_name = 'App User'
        verbose_name_plural = 'App Users'


class EmployeeData(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='employee_data')

    street_address = models.CharField(max_length=100, null=True, blank=True)
    street_address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=5, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Employee Data'
        verbose_name_plural = verbose_name


class ClientData(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='client_data')
    starred = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Client Data'
        verbose_name_plural = verbose_name
