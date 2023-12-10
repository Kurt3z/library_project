import uuid
from django.db import models
from .publisher import Publisher
from .genre import Genre


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    title = models.CharField(max_length=250)
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    quantity = models.PositiveIntegerField(default=1)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.SET_DEFAULT, default="Editora não especificada")
    genre = models.ManyToManyField(Genre)
