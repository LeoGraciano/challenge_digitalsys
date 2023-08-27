from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.core import views

urlpatterns = [
    path('', views.test),
]