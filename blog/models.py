# models.py

from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    data = models.TextField()

    def __str__(self):
        return self.title
