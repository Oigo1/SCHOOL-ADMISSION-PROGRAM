# Generated by Django 4.1.3 on 2024-09-05 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=100)),
                ("middle_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("class_year", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Fee",
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
                ("amount_paid", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total_fee", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admissions.student",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ActivityStatus",
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
                ("bus", models.BooleanField(default=False)),
                ("library", models.BooleanField(default=False)),
                ("lunch", models.BooleanField(default=False)),
                ("swimming", models.BooleanField(default=False)),
                ("exams", models.BooleanField(default=False)),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admissions.student",
                    ),
                ),
            ],
        ),
    ]