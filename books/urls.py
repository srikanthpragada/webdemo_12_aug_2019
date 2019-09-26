
from django.contrib import admin
from django.urls import path
from . import views, books_views

urlpatterns = [
    path("index/", views.welcome),
    path("welcome/", views.welcome),
    path("countries/", views.list_countries),
    path("addauthor/", views.add_author),
    path("updateauthor/", views.update_author),
    path("home/", books_views.books_home),
    path("list/", books_views.books_list),
    path("add/", books_views.books_add),
    path("delete/<int:id>", books_views.books_delete),
    path("edit/<int:id>", books_views.books_edit),
]

