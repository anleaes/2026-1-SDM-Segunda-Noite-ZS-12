from .models import Student
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'cpf', 'email', 'matricula', 'data_nascimento', 'status']