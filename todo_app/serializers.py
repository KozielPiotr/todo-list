"""Serializers for todo_app models"""

from rest_framework.serializers import ModelSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    """Serializer for Task model"""
    class Meta:
        """Meta class to prevent error"""
        model = Task
        fields = ("id", "name", "description", "add_date", "done")
