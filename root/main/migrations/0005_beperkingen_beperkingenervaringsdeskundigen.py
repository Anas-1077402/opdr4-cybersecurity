# Generated by Django 5.0.2 on 2024-03-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_deelnames"),
    ]

    operations = [
        migrations.CreateModel(
            name="Beperkingen",
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
                ("omschrijving", models.TextField()),
                ("soort", models.TextField()),
            ],
            options={
                "db_table": "Beperkingen",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="BeperkingenErvaringsdeskundigen",
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
                ("beperking_id", models.IntegerField()),
                ("ervaringsdeskundigen_id", models.IntegerField()),
            ],
            options={
                "db_table": "Beperkingen_ervaringsdeskundigen",
                "managed": False,
            },
        ),
    ]
