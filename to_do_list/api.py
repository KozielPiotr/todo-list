"""Router for api"""

from rest_framework import routers

from todo_app import api_views


router = routers.DefaultRouter()
router.register("tasks", api_views.TaskViewset)
