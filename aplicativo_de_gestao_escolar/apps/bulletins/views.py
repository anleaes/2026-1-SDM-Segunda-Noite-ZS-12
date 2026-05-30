from django.shortcuts import render
from rest_framework import viewsets
from .models import Bulletins
from .serializer import BulletinsSerializer

# Create your views here.
class BulletinsViewSet(viewsets.ModelViewSet):
    queryset = Bulletins.objects.all()
    serializer_class = BulletinsSerializer  