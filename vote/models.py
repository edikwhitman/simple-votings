import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

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
    link = models.CharField(max_length=100, default='')
    text = models.CharField(max_length=300, default='')

    STATUS = (
        ('u', 'Unchecked'),
        ('c', 'Checked'),
    )

    status = models.CharField(max_length=1, choices=STATUS, default='u')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=''
    )

    def _str_(self):
        return self.text[:10]


class CheckedVotings(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default="")  # пользователь, просмотревший голосование
    voting_id = models.ForeignKey(to=VoteModel, on_delete=models.CASCADE, default="")  # голосование, которое пользователь просмотрел

