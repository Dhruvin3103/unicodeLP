# Generated by Django 4.1.1 on 2022-11-01 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoL', '0009_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
