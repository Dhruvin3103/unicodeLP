# Generated by Django 4.1.1 on 2022-12-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theatre_name', models.CharField(max_length=100)),
                ('theatre_no', models.CharField(max_length=100, unique=True)),
                ('theatre_add', models.TextField(max_length=1000)),
                ('theatre_capacity', models.IntegerField(default=50)),
                ('no_of_theatre', models.TimeField()),
            ],
        ),
    ]