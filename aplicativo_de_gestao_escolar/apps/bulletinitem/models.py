from django.db import models


class Bulletinitem(models.Model):
    final_grade = models.FloatField('Final Grade')
    frequency = models.FloatField('Frequency')
    situation = models.CharField('Situation', max_length=50)

    bulletin = models.ForeignKey(
        'bulletins.Bulletins',
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Bulletins'
    )
    discipline = models.ForeignKey(
        'disciplines.Discipline',
        on_delete=models.CASCADE,
        related_name='bulletinitem',
        verbose_name='Disciplines'
    )

    class Meta:
        verbose_name = 'Bulletin Item'
        verbose_name_plural = 'Bulletin Items'
        ordering = ['id']

    def __str__(self):
        return f'{self.discipline} - {self.situation}'