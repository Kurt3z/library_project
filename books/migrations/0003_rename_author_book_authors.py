# Generated by Django 5.0 on 2023-12-15 22:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_book_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="author",
            new_name="authors",
        ),
    ]
