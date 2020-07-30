from django.contrib import admin
from django.urls import path,include
from App import views

urlpatterns = [
    path("", views.index, name='App'),
    path("contact", views.contact, name='Contact'),
    path("symptoms", views.symptoms, name='symptoms'),
    path("donate", views.donate, name='donate')
]