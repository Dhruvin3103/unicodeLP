# Generated by Django 4.1.1 on 2023-01-10 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0024_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 10, 10, 52, 59, 850028)),
        ),
    ]
