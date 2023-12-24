import uuid
from django.db import models
from .contact import Contact


class Librarian(Contact):
    salary = models.DecimalField(max_digits=6, decimal_places=2, null=True)
