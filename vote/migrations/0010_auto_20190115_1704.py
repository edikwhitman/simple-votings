# Generated by Django 2.1.3 on 2019-01-15 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0009_auto_20190111_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votemodel',
            name='closing_poll_datetime',
        ),
        migrations.AddField(
            model_name='votemodel',
            name='closing_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 16, 17, 4, 56, 975823)),
        ),
    ]
