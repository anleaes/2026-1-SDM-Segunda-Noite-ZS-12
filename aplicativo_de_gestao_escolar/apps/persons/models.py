from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()