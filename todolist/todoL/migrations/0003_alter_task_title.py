# Generated by Django 4.1.1 on 2022-10-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoL', '0002_alter_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
