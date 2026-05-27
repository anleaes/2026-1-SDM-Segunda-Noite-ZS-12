from django.db import models
from persons.models import Person

# Create your models here.
class Teacher(Person):
    TITULACAO_CHOICES = [
        ('graduado', 'Graduado'),
        ('especialista', 'Especialista'),
        ('mestre', 'Mestre'),
        ('doutor', 'Doutor'),
    ]
    titulacao = models.CharField('titulacao', max_length=20, choices=TITULACAO_CHOICES)
    registro = models.CharField('registro', max_length=20)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.name