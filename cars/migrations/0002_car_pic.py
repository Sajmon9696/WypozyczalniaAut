# Generated by Django 5.0.1 on 2024-02-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="pic",
            field=models.ImageField(blank=True, null=True, upload_to="img/"),
        ),
    ]
