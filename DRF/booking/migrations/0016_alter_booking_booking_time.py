# Generated by Django 4.1.1 on 2023-01-01 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 11, 48, 15, 892026)),
        ),
    ]