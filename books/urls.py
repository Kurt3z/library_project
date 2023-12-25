from django.urls import path
from . import views

urlpatterns = [
    path("", views.listBooks, name="books"),
    path("add-book", views.addBook, name="add-book"),
    path("add-author", views.addAuthor, name="add-author")
]
