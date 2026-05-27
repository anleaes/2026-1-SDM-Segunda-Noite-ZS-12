from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'classes'

router = routers.SimpleRouter()
router.register('', views.CategoryViewSet, basename='classes')

urlpatterns = [
    path('', include(router.urls) )
]