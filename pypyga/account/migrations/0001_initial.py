# Generated by Django 4.1 on 2022-08-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccountModel",
            fields=[
                ("id", models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]