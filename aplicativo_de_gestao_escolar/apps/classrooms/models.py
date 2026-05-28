from django.db import models

# Create your models here.
class Classroom(models.Model):
    data = models.DateField('Data')
    sala = models.CharField('Sala', max_length=30)
    conteudo = models.TextField('Conteúdo', max_length=255)

    # Relacionamentos
    registration = models.ForeignKey(
        'registrations.Registration',
        on_delete=models.CASCADE,
        related_name='classrooms',
        verbose_name='Matrícula'
    )

    discipline = models.ForeignKey(
        'disciplines.Discipline',
        on_delete=models.CASCADE,
        related_name='classrooms',
        verbose_name='Disciplina'
    )

