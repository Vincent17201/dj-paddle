# Generated by Django 5.0a1 on 2023-10-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djpaddle", "0004_auto_20210119_0436"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="alert_id",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
