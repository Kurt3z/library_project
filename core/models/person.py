import uuid
from django.db import models


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()
