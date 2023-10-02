# accounts/urls.py

from django.urls import path
from .views import index, custom_login, custom_logout, custom_register, profile

app_name = 'accounts'

urlpatterns = [
    path('', index, name='index'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', custom_register, name='register'),
    path('profile/', profile, name='profile'),
]
