# Generated by Django 2.1.4 on 2019-01-20 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20190120_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votemodel',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 20, 11, 58, 2, 873182)),
        ),
    ]
