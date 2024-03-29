"""Router for api"""

from rest_framework import routers
from django.urls import include, path

from . import views


router = routers.DefaultRouter()
router.register("tasks", views.TaskViewset)

urlpatterns = [
    path("", include(router.urls))
]
