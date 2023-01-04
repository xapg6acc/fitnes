# Generated by Django 4.1.4 on 2022-12-08 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BodyShape",
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
                ("height", models.IntegerField(blank=True, null=True)),
                ("weight", models.IntegerField(blank=True, null=True)),
                ("waist", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Day",
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
                ("day", models.DateField()),
                ("water", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Exercise",
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
                (
                    "type",
                    models.CharField(
                        choices=[("Workout", "Workout"), ("Stretching", "Stretching")],
                        max_length=20,
                    ),
                ),
                ("info", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=63)),
                ("video", models.URLField()),
                ("sets", models.IntegerField()),
                ("reps", models.IntegerField()),
                ("time_per_rep", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Muscle",
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
                ("title", models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name="Training",
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
                ("name", models.CharField(max_length=63)),
                ("comment", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "day",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="app.day"
                    ),
                ),
                ("muscles", models.ManyToManyField(to="app.muscle")),
            ],
        ),
    ]
