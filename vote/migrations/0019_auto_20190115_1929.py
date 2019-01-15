# Generated by Django 2.1.3 on 2019-01-15 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0018_auto_20190115_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkedvoting',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='checkedvoting',
            name='voting_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vote.VoteModel'),
        ),
        migrations.AlterField(
            model_name='votemodel',
            name='creation_time',
            field=models.DateTimeField(default=''),
        ),
    ]
