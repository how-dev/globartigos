# Generated by Django 4.2.7 on 2023-12-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categoriesmodel",
            name="name",
            field=models.CharField(max_length=255, unique=True, verbose_name="Name"),
        ),
    ]