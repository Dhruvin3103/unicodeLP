# Generated by Django 4.1.1 on 2022-10-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoL', '0002_alter_user_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='imgs',
            field=models.ImageField(upload_to='image/'),
        ),
    ]