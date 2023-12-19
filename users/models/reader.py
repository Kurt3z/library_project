import uuid
from django.db import models
from .contact import Contact


class Reader(Contact):
    reader_id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False)
    requisition_count = models.PositiveIntegerField(default=0)
    fines_value = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)
