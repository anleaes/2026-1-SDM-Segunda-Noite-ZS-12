from django.shortcuts import render
from rest_framework import viewsets
from .models import Bulletinitem
from .serializer import BulletinitemSerializer



class BulletinitemViewSet(viewsets.ModelViewSet):
    queryset = Bulletinitem.objects.all()
    serializer_class = BulletinitemSerializer  