# Generated by Django 4.2.6 on 2023-12-01 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CrimeSceneReport",
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
                ("date", models.DateField()),
                ("location", models.TextField()),
                ("officer", models.TextField()),
                ("description", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Job",
        ),
    ]
