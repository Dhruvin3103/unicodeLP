# Generated by Django 4.1.1 on 2023-01-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapi', '0007_alter_user_mob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mob',
            field=models.IntegerField(default=9000000000, max_length=10),
        ),
    ]
