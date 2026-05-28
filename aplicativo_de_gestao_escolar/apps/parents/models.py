from django.db import models
from persons.models import Person

# Create your models here.

class Parent(Person):
    PARENTESCO_CHOICES = [
    ('pai', 'Pai'),
    ('mae', 'Mãe'),
    ('avo', 'Avô/Avó'),
    ('tio', 'Tio/Tia'),
    ('responsavel_legal', 'Responsável Legal'),
    ]
    responsavel_financeiro = models.BooleanField(default=False)
    parentesco = models.CharField(max_length=20, choices=PARENTESCO_CHOICES)


    class Meta:
        verbose_name = 'Responsavel'
        verbose_name_plural = 'Responsaveis'
        ordering = ['id']

    def __str__(self):
        return self.name