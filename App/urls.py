from django.contrib import admin
from django.urls import path,include
from App import views

urlpatterns = [
    path("", views.index, name='App'),
    path("contact", views.contact, name='Contact'),
    path("ref", views.ref, name='Ref'),
    path("variable", views.variable, name='variable')
]