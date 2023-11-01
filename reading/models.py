# reading/models.py

from django.db import models

class Reading(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    genre = models.CharField(max_length=100)
    length = models.IntegerField()
