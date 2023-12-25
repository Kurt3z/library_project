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
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(
        max_length=200, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=500, null=True)
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    street = models.CharField(max_length=500, null=True, blank=True)
    building = models.PositiveIntegerField(null=True, blank=True)
    postal_code = models.CharField(max_length=8, null=True, blank=True, validators=[
        RegexValidator(regex="^\d{4}-\d{3}$", message="Insira um Código-Postal válido.")])
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True, blank=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to="profiles/", default="user-default.png")
    is_librarian = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
