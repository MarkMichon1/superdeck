from django.conf.urls import url
from django.urls import path

from frontend.views import about, article_detail, ArticleListView, contact, home, services


urlpatterns = [
    path('', home, name='frontend-home'),
    path('services/', about, name='frontend-services'),
    path('articles/', ArticleListView, name='frontend-articles'),
    path('articles/<slug:url_slug>/', article_detail, name='frontend-article-detail'),
    path('contact/', contact, name='frontend-contact'),
    path('services/', services, name='frontend-services'),
]