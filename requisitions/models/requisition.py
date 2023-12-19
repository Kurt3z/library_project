import uuid
from datetime import timedelta
from django.utils import timezone
from django.db import models

from users.models import Librarian, Reader
from core.models import Content
from .tier import Tier


class Requisition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    librarian = models.ForeignKey(
        Librarian, on_delete=models.SET_NULL, null=True)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    content = models.ManyToManyField(Content)
    tier = models.ForeignKey(Tier, on_delete=models.PROTECT)
    fine = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, editable=False)
    return_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def calc_return_date(self):
        return_date = self.created + timedelta(weeks=2)
        return return_date

    def calc_fine(self):
        if not self.is_active:
            return 0

        days_difference = (timezone.now() - self.return_date).days

        if days_difference > 0:
            fine_value = self.tier.fine * days_difference
            self.reader.fines_value += fine_value
            self.reader.save()

        return fine_value

    def save(self, *args, **kwargs):
        self.return_date = self.calc_return_date()
        self.fine = self.calc_fine()
        super().save(*args, **kwargs)
