# Generated by Django 5.0 on 2023-12-24 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_contact_is_librarian"),
    ]

    operations = [
        migrations.AlterField(
            model_name="librarian",
            name="salary",
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
