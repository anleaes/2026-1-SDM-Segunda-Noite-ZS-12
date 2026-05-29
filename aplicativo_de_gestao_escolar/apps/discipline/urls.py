from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'discipline'

router = routers.SimpleRouter()
router.register('', views.DisciplineViewSet, basename='disciplina')

urlpatterns = [
    path('', include(router.urls) )
]
