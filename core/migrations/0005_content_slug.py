# Generated by Django 5.0 on 2023-12-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_content_language_content_summary_alter_country_flag"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="slug",
            field=models.SlugField(blank=True, default=""),
        ),
    ]
