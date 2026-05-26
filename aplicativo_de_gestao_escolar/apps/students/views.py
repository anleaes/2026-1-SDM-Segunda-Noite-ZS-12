from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializer import PersonSerializer
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer  
