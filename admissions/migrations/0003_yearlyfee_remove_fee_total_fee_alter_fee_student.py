# Generated by Django 4.1.3 on 2024-09-09 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0002_alter_fee_amount_paid"),
    ]

    operations = [
        migrations.CreateModel(
            name="YearlyFee",
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
                ("total_fee", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name="fee",
            name="total_fee",
        ),
        migrations.AlterField(
            model_name="fee",
            name="student",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="admissions.student"
            ),
        ),
    ]
