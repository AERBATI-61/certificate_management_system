from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', loginUser, name='login'),
    path('loginout/', logoutUser, name='logout'),
    # path('register/', register, name='register'),
]