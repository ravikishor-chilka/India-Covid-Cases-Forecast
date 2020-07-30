from django.contrib import admin
from django.urls import path,include
from App import views

urlpatterns = [
    path("", views.index, name='App'),
    path("donate", views.donate, name='Donate'),
    path("symptoms", views.symptoms, name='Symptoms'),
    path("contact", views.contact, name='Contact')
]