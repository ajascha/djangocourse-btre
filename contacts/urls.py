# Mostly copied from another app's urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
]