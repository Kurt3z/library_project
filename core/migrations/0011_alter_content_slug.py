# Generated by Django 4.2.8 on 2023-12-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_alter_publisher_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
