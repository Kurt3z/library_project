# Generated by Django 5.0 on 2023-12-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_remove_librarian_librarian_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="is_librarian",
            field=models.BooleanField(default=False),
        ),
    ]
