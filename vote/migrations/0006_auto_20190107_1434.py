# Generated by Django 2.1.3 on 2019-01-07 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0005_auto_20190106_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='votemodel',
            old_name='question',
            new_name='questions',
        ),
    ]