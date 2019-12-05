"""Models for todo_app"""

from django.db import models


class Task(models.Model):
    """Model for task object"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    add_date = models.DateField(auto_now=True)
    done = models.BooleanField(default=False)
