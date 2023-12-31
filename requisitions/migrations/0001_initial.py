# Generated by Django 5.0 on 2023-12-19 15:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0006_rename_creation_date_content_created_and_more"),
        ("users", "0002_contact_district"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tier",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("tier", models.CharField(max_length=1)),
                ("description", models.TextField(max_length=500)),
                ("fine", models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name="Requisition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "fine",
                    models.DecimalField(decimal_places=2, default=0, max_digits=5),
                ),
                ("return_date", models.DateTimeField()),
                ("content", models.ManyToManyField(to="core.content")),
                (
                    "librarian",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.librarian",
                    ),
                ),
                (
                    "reader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.reader"
                    ),
                ),
                (
                    "tier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="requisitions.tier",
                    ),
                ),
            ],
        ),
    ]
