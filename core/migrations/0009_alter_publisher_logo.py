# Generated by Django 4.2.8 on 2023-12-23 01:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_alter_country_flag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publisher",
            name="logo",
            field=models.ImageField(blank=True, upload_to="images/publisher_logos"),
        ),
    ]
