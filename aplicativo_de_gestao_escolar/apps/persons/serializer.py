from rest_framework import viewsets
from .models import Person
from .serializer import PersonSerializer

class Person(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer