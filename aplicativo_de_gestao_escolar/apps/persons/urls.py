from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'persons'

router = routers.SimpleRouter()
router.register('', views.PersonViewSet, basename='persons')

urlpatterns = [
    path('', include(router.urls) )
]