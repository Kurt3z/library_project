import uuid
from django.db import models


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    flag = models.ImageField(upload_to="images/country_flags/")
