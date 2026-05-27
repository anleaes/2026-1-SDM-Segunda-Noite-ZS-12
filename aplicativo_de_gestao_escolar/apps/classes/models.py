from django.db import models

# Create your models here.
class Turma(models.Model):
    codigo = models.CharField('Código', max_length=20)
    turno = models.CharField('Turno', max_length=20)
    ano_letivo = models.IntegerField('Ano Letivo')

