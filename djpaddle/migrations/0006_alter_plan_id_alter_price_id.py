# Generated by Django 5.0a1 on 2024-01-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djpaddle", "0005_subscription_alert_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plan",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
