from django.db import models

from datetime import time

class Instance(models.Model):
    is_initialized = models.BooleanField(default=False)
    is_opened = models.BooleanField(default=True) #these and below - abstracted out into own model as company grows
    opening_time = models.TimeField(default=time(9, 0, 0))
    closing_time = models.TimeField(default=time(17, 0, 0))

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Instance, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        loaded_object, created = cls.objects.get_or_create(pk=1)
        return loaded_object


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


class LoggedEmail(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)