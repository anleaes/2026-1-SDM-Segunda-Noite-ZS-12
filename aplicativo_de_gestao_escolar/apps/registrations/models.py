from django.db import models

# Create your models here.
class Registration(models.Model):
    data_matricula = models.DateField('Data da Matrícula')
    situacao = models.CharField('Situação', max_length=30)

    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='registrations',
        verbose_name='Aluno'
    )

    school_class = models.ForeignKey(
        'classes.Class',
        on_delete=models.CASCADE,
        related_name='registrations',
        verbose_name='Turma'
    )

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        ordering = ['id']

    def __str__(self):
        return f'{self.id} - {self.situacao}'