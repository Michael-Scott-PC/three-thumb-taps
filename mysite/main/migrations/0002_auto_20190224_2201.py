# Generated by Django 2.1.7 on 2019-02-25 03:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 24, 22, 1, 33, 264274), verbose_name='date published'),
        ),
    ]