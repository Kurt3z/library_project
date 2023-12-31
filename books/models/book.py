from django.db import models
from django.core.validators import RegexValidator
from core.models import Content
from .author import Author


class Book(Content):
    isbn = models.CharField(max_length=13, validators=[
                            RegexValidator(regex="^(97(8|9))?\d{9}(\d|X)$", message="Insira um ISBN.")])
    pages = models.PositiveIntegerField()
    format = models.CharField(max_length=10, choices=[(
        "hardcover", "Capa Dura"), ("paperback", "Capa Mole")])
    cover = models.ImageField(upload_to="images/books/")
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return self.title
