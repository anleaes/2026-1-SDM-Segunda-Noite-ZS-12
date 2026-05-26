from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'students'

router = routers.SimpleRouter()
router.register('', views.StudentViewSet, basename='students')
urlpatterns = [
    path('', include(router.urls) )
]
