from django.db import models

from django.db import models

class Discipline(models.Model):
    name = models.CharField('Name', max_length=100)
    workload = models.IntegerField('Workload')
    code = models.CharField('Code', max_length=20)
