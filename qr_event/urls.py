from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.join, name='join'),
    path('home/<str:event_code>', views.home, name='home')
]
