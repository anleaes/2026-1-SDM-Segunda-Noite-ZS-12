from .models import Student
from rest_framework import serializers
from parents.serializers import ParentSerializer

class StudentSerializer(serializers.ModelSerializer):
    responsaveis = ParentSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'cpf', 'email', 'matricula', 'data_nascimento', 'status', 'responsaveis']
