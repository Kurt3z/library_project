# Generated by Django 5.0 on 2023-12-19 14:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_content_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="content",
            old_name="creation_date",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="country",
            old_name="creation_date",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="genre",
            old_name="creation_date",
            new_name="created",
        ),
        migrations.RenameField(
            model_name="publisher",
            old_name="creation_date",
            new_name="created",
        ),
    ]
