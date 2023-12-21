# Generated by Django 4.2.8 on 2023-12-20 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_contact_district"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                max_length=1,
                null=True,
            ),
        ),
    ]