# pylint: disable = too-many-ancestors, no-member
"""Views for todo_app api"""

from rest_framework import viewsets

from . import models, serializers


class TaskViewset(viewsets.ModelViewSet):
    """View for Task model"""
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
