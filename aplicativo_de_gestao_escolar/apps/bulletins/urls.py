from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'bulletins'

router = routers.SimpleRouter()
router.register('', views.BulletinsViewSet, basename='boletins')

urlpatterns = [
    path('', include(router.urls) )
]