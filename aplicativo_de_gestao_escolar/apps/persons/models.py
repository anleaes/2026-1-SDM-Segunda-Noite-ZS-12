from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()

class Meta:
    verbose_name = 'Pessoa'
    verbose_name_plural = 'Pessoas'
    ordering = ['id']

def __str__(self): 
    return self.name