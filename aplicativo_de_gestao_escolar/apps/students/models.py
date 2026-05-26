from django.db import models
from persons.models import Person

# Create your models here.
class Student(Person):
    matricula = models.CharField('Matricula', max_length=20, unique=True)
    dataNascimento = models.CharField('Data de nascimento,',max_length=10)
    status = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('Trancado', 'Trancado'),
    ]

class Meta:
    verbose_name = 'Aluno'
    verbose_name_plural = 'Alunos'
    ordering = ['id']

def __str__(self): 
    return self.name