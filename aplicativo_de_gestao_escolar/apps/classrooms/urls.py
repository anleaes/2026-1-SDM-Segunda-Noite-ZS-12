from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'classrooms'

router = routers.SimpleRouter()
router.register('', views.ClassroomViewSet, basename='classrooms')

urlpatterns = [
    path('', include(router.urls) )
]