from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'registrationcarts'

router = routers.SimpleRouter()
router.register('', views.RegistrationCartViewSet, basename='registrationcart')

urlpatterns = [
    path('', include(router.urls) )
]