
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.welcome),
    path("welcome/", views.welcome),
    path("countries/", views.list_countries),
    path("addauthor/", views.add_author),
    path("updateauthor/", views.update_author),
]
