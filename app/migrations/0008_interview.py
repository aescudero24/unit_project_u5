# Generated by Django 4.2.6 on 2023-12-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_librarycard"),
    ]

    operations = [
        migrations.CreateModel(
            name="Interview",
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
                ("personal_id", models.IntegerField()),
                ("description", models.TextField()),
            ],
        ),
    ]
