from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'teachers'
router = routers.SimpleRouter()
router.register('',views.TeacherViewSet, basename='professores')

urlpatterns = [ 
    path('', include(router.urls))
]