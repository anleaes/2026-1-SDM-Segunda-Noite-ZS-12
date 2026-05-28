from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'registrations'

router = routers.SimpleRouter()
router.register('', views.RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('', include(router.urls) )
]