from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'grades'

router = routers.SimpleRouter()
router.register('', views.GradeViewSet, basename='notas')

urlpatterns = [
    path('', include(router.urls) )
]

