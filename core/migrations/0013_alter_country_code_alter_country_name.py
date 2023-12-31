# Generated by Django 5.0 on 2023-12-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0012_alter_genre_caption"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="code",
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
