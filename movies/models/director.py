from django.db import models
from core.models import Person
from core.models import Country


class Director(Person):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    biography = models.TextField(blank=True)
    picture = models.ImageField(upload_to="images/directors/")
