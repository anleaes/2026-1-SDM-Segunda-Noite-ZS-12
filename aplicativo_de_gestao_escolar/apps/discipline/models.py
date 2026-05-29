from django.db import models

from django.db import models

class Discipline(models.Model):
    name = models.CharField('Name', max_length=100)
    workload = models.IntegerField('Workload')
    code = models.CharField('Code', max_length=20)

    class Meta:
        verbose_name = 'Discipline'
        verbose_name_plural = 'Disciplines'
        ordering = ['id']

    def __str__(self):
        return f'{self.code} - {self.name}'