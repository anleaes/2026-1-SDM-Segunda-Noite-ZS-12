from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'disciplines'

router = routers.SimpleRouter()
router.register('', views.DisciplineViewSet, basename='disciplinas')

urlpatterns = [
    path('', include(router.urls) )
]


