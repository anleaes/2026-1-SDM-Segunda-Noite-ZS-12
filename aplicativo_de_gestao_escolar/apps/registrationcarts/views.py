from django.shortcuts import render
from rest_framework import viewsets
from .models import RegistrationCart
from .serializer import RegistrationCartSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = RegistrationCart.objects.all()
    serializer_class = RegistrationCartSerializer  