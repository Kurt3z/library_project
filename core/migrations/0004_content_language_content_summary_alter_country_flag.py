# Generated by Django 5.0 on 2023-12-15 22:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_alter_content_publisher"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="language",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.PROTECT,
                to="core.country",
            ),
        ),
        migrations.AddField(
            model_name="content",
            name="summary",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="country",
            name="flag",
            field=models.ImageField(upload_to="images/country-flags/"),
        ),
    ]