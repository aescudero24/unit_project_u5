# Generated by Django 4.2.6 on 2023-12-04 04:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_driverslicense"),
    ]

    operations = [
        migrations.CreateModel(
            name="LibraryCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_name", models.TextField()),
                ("aisle", models.IntegerField()),
                ("books", models.IntegerField()),
            ],
        ),
    ]
