# Generated by Django 4.1.1 on 2023-01-01 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_alter_payment_p_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='p_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 1, 12, 48, 17, 719978)),
        ),
    ]
