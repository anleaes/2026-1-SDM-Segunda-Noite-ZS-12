from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'parents'

router = routers.SimpleRouter()
router.register('', views.ParentViewSet, basename='responsaveis')

urlpatterns = [
    path('', include(router.urls))
]