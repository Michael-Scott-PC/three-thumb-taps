# Generated by Django 2.1.7 on 2019-03-01 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190301_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 1, 14, 28, 11, 513950), verbose_name='date published'),
        ),
    ]
