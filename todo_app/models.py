"""Models for todo_app"""

from django.db import models


class Task(models.Model):
    """Model for task object"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    term = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)
