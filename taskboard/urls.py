from rest_framework import routers
from django.urls import path, include
from .views import BoardViewSet, TaskViewSet, index

router = routers.DefaultRouter()
router.register('boards', BoardViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', index, name='homepage'),
    path('api/', include(router.urls))
]

