from rest_framework import viewsets
from .models import Grades
from .serializer import GradesSerializer

class GradesViewSet(viewsets.ModelViewSet):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer  