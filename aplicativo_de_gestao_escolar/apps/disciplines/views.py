from django.shortcuts import render

from rest_framework import viewsets
from .models import Discipline
from .serializer import DisciplineSerializer

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer  


