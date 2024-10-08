# Generated by Django 5.1 on 2024-09-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SafetyPoint",
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
                ("name", models.CharField(max_length=100)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("point_type", models.CharField(max_length=50)),
            ],
        ),
    ]
