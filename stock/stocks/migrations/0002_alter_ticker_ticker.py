# Generated by Django 4.2.10 on 2024-02-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='ticker',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]