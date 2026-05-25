from django.db import models
from persons.models import Person

# Create your models here.
class Student(Person):
    matricula = models.CharField('Matricula', max_length=20, unique=True)
    dataNascimento = models.CharField('Data de nascimento,',max_length=10)