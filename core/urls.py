from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-publisher", views.addPublisher, name="add-publisher"),
    path("add-genre", views.addGenre, name="add-genre"),
    path("add-country", views.addCountry, name="add-country"),
]
