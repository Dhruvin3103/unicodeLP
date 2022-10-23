# Generated by Django 4.1.1 on 2022-10-20 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('task_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoL.task')),
            ],
        ),
    ]
