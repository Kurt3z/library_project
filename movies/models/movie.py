from django.db import models
from core.models import Content
from .director import Director


class Movie(Content):
    duration_minutes = models.PositiveIntegerField()
    media_type = models.CharField(max_length=10)
    cover = models.ImageField(upload_to="images/movies/")
    trailer = models.URLField()
    directors = models.ManyToManyField(Director, related_name="movies")
