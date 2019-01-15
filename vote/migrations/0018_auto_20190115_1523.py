# Generated by Django 2.1.3 on 2019-01-15 12:23

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0017_auto_20190113_2110'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CheckedVotings',
            new_name='CheckedVoting',
        ),
        migrations.AlterField(
            model_name='votemodel',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 15, 23, 49, 835913)),
        ),
    ]
