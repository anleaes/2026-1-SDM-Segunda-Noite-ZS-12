from django.db import models
from persons.models import Person

# Create your models here.
class Student(Person):
    matricula = models.CharField('Matricula', max_length=20, unique=True)
    data_nascimento = models.CharField('Data de nascimento,',max_length=10, )
   
   
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('Trancado', 'Trancado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

class Meta:
    verbose_name = 'Aluno'
    verbose_name_plural = 'Alunos'
    ordering = ['id']

def __str__(self): 
    return self.name