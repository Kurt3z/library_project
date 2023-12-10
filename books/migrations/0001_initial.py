# Generated by Django 5.0 on 2023-12-10 20:59

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0003_alter_content_publisher"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("birthdate", models.DateField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("biography", models.TextField(blank=True)),
                ("personal_website", models.URLField(blank=True, null=True)),
                ("picture", models.ImageField(upload_to="images/authors/")),
                (
                    "country",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.country",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "content_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.content",
                    ),
                ),
                (
                    "isbn",
                    models.CharField(
                        max_length=13,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Insira um ISBN.",
                                regex="^(97(8|9))?\\d{9}(\\d|X)$",
                            )
                        ],
                    ),
                ),
                ("pages", models.PositiveIntegerField()),
                (
                    "format",
                    models.CharField(
                        choices=[
                            ("hardcover", "Capa Dura"),
                            ("paperback", "Capa Mole"),
                        ],
                        max_length=10,
                    ),
                ),
                ("cover", models.ImageField(upload_to="images/books/")),
                (
                    "author",
                    models.ManyToManyField(related_name="books", to="books.author"),
                ),
            ],
            bases=("core.content",),
        ),
    ]
