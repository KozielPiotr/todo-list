"""Serializers for todo_app models"""

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from .models import Task


class TaskSerializer(ModelSerializer):
    """Serializer for Task model"""
    url = HyperlinkedIdentityField(view_name="task-detail")

    class Meta:
        """Meta class to prevent error"""
        model = Task
        exclude = ["id"]

