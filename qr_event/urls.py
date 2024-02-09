# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
