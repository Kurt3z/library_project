import uuid
from django.db import models


class Tier(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    tier = models.CharField(max_length=1)
    description = models.TextField(max_length=500)
    fine = models.DecimalField(max_digits=4, decimal_places=2)
