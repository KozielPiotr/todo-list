# pylint: disable = too-many-ancestors, no-member
"""Views for todo_app api"""

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from . import models, serializers


class TaskViewset(viewsets.ModelViewSet):
    """View for Task model"""
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

    @action(detail=False, methods=["GET"])
    def recent(self, request, *args, **kwargs):
        today = timezone.now().date()
        queryset = self.get_queryset().filter(term=today)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
