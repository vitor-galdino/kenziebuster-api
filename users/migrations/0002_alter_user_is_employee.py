# Generated by Django 4.2 on 2023-04-11 20:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(default=False),
        ),
    ]
