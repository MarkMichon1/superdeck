from django.db import models


class Instance(models.Model):
    is_initialized = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Instance, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        loaded_object, created = cls.objects.get_or_create(pk=1)
        return loaded_object
