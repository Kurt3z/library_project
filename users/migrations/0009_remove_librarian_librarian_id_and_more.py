# Generated by Django 4.2.8 on 2023-12-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_contact_birthdate_alter_contact_building_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="librarian",
            name="librarian_id",
        ),
        migrations.RemoveField(
            model_name="reader",
            name="reader_id",
        ),
        migrations.AlterField(
            model_name="contact",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="first_name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="last_name",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
