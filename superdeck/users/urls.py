from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='users-token-create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='users-token-refresh')
]