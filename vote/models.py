from django.db import models

# Create your models here.


class Vote(models.Model):
    name = models.CharField(max_length=100, default='')
    text = models.CharField(max_length=300, default='')
    options = models.CharField(max_length=500, default='')
