# Generated by Django 3.2 on 2022-02-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_cars_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.TextField(blank=True, verbose_name='История'),
        ),
    ]
