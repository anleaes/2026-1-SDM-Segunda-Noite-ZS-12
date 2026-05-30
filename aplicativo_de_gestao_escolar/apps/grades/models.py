from django.db import models

class Grades(models.Model):
    bimester = models.IntegerField('Bimester')
    value = models.FloatField('Value')
    type = models.CharField('Type', max_length=50)

    bulletin = models.ForeignKey(
        'bulletins.Bulletins',
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name='Bulletins'
    )
    class Meta:
        verbose_name = 'Notas'
        verbose_name_plural = 'Notas'
        ordering = ['id']

    def __str__(self):
        return f'Bimester {self.bimester} - {self.type}: {self.value}'