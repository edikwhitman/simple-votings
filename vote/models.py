import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class VoteModel(models.Model):
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
    creation_time = models.DateTimeField(default=datetime.datetime.now())
    ref = models.CharField(max_length=500, default='')
    question = models.CharField(max_length=100, default='')
    options = models.CharField(max_length=500, default='')

    TYPES = (
        ('o', 'One of many'),
        ('s', 'Several of many'),
        ('d', 'discrete'),
    )

    type = models.CharField(max_length=1, choices=TYPES, default='o')

    def __str__(self):
        return self.question


class ReportModel(models.Model):
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
    link = models.CharField(max_length=100, default='')
    text = models.CharField(max_length=300, default='')

    def _str_(self):
        return self.text[:10]


class CheckedVotings(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)  # пользователь, просмотревший голосование
    voting_id = models.ForeignKey(to=VoteModel, on_delete=models.CASCADE)  # голосование, которое пользователь просмотрел

