# Generated by Django 4.1.1 on 2023-01-01 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payment_p_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='p_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 11, 40, 57, 245527)),
        ),
    ]
