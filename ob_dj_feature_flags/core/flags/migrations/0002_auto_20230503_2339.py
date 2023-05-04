# Generated by Django 3.1.14 on 2023-05-03 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flags", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="featureflag",
            name="name",
            field=models.CharField(
                help_text="Name of the flag", max_length=50, unique=True
            ),
        ),
    ]