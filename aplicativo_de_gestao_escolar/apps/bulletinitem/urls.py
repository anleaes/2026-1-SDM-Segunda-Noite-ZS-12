from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'bulletinitems'

router = routers.SimpleRouter()
router.register('', views.CategoryViewSet, basename='itemboletim')

urlpatterns = [
    path('', include(router.urls) )
]