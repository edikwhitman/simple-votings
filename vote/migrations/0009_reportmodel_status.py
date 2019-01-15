# Generated by Django 2.1.3 on 2019-01-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0008_reportmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportmodel',
            name='status',
            field=models.CharField(choices=[('u', 'Unchecked'), ('c', 'Checked')], default='u', max_length=1),
        ),
    ]
