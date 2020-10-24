from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import AppUser, ClientData, EmployeeData

@receiver(post_save, sender=AppUser)
def user_post_save_create_extended_data(sender, instance, created, **kwargs):
    if created:
        if instance.get_user_type_humanize() == 'Client':
            ClientData.objects.create(user=instance)
        else:
            EmployeeData.objects.create(user=instance)