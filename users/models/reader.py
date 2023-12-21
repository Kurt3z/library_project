import uuid
from django.db import models
from .contact import Contact


class Reader(Contact):
    requisition_count = models.PositiveIntegerField(default=0, editable=False)
    fines_value = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
