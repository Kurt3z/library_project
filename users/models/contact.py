import uuid
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

from .district import District


class Contact(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    street = models.CharField(max_length=500)
    building = models.PositiveIntegerField()
    postal_code = models.CharField(max_length=8, validators=[
        RegexValidator(regex="^\d{4}-\d{3}$", message="Insira um Código-Postal válido.")])
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
