import uuid

from django.db import models
from django.conf import settings

# Create your models here.


class VoteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular voting")
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
