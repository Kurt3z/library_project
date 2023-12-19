import uuid
from django.db import models
from .contact import Contact


class Librarian(Contact):
    librarian_id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
