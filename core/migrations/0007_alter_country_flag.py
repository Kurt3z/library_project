# Generated by Django 4.2.8 on 2023-12-23 01:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_rename_creation_date_content_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="flag",
            field=models.ImageField(null=True, upload_to="images/country-flags/"),
        ),
    ]
