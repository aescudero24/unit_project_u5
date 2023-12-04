# Generated by Django 4.2.6 on 2023-12-04 03:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_delete_driverslicense"),
    ]

    operations = [
        migrations.CreateModel(
            name="DriversLicense",
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
                ("license_id", models.IntegerField()),
                ("age", models.IntegerField()),
                ("height", models.IntegerField()),
                ("hair_color", models.TextField()),
                ("gender", models.TextField()),
            ],
        ),
    ]
