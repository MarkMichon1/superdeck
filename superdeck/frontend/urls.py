from django.conf.urls import url
from django.urls import path

from frontend.views import about, articles, contact, home, services


urlpatterns = [
    path('', home, name='frontend-home'),
    path('services/', about, name='frontend-services'),
    path('articles/', articles, name='frontend-articles'),
    path('contact/', contact, name='frontend-contact'),
    path('services/', services, name='frontend-services'),
]