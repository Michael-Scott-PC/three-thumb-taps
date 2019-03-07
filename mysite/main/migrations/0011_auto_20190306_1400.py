# Generated by Django 2.1.7 on 2019-03-06 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190306_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='confirmed_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 6, 14, 0, 9, 308443), verbose_name='date published'),
        ),
    ]
