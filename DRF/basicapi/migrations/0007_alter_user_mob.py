# Generated by Django 4.1.1 on 2023-01-01 06:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapi', '0006_user_is_movie_operator_user_is_theatre_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mob',
            field=models.IntegerField(default=9000000000, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
