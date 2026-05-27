from django.db import models

# Create your models here.
class Turma(models.Model):
    codigo = models.CharField('Código', max_length=20)
    turno = models.CharField('Turno', max_length=20)
    ano_letivo = models.IntegerField('Ano Letivo')

    professor = models.ForeignKey(
        'Professor',
        on_delete=models.CASCADE,
        related_name='Turmas',
        verbose_name='Professor'
    )

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['id']

    def __str__(self):
        return f'{self.codigo} - {self.turno} ({self.ano_letivo})'