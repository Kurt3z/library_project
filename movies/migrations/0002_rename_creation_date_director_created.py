# Generated by Django 5.0 on 2023-12-19 14:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="director",
            old_name="creation_date",
            new_name="created",
        ),
    ]
