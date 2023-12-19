import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import Content
from users.models import Reader


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(max_length=1000, null=True, blank=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    reder = models.ForeignKey(Reader, on_delete=models.CASCADE)
