from django.db import models

from users.models import EmployeeData


class Article(models.Model):
    author = models.OneToOneField(EmployeeData, on_delete=models.SET_NULL, null=True, related_name='articles')
    datetime_added = models.DateTimeField(auto_now_add=True)
    url_slug = models.SlugField(max_length=55, unique=True)
    html_body = models.TextField()

    class Meta:
        ordering = ['-datetime_added']


class ContactMessage(models.Model):
    datetime_sent = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    message_body = models.TextField(max_length=5000)  # todo enforce this on SPA
