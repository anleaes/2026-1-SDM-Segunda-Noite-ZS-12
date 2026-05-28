from django.db import models

# Create your models here.
class RegistrationCart(models.Model):
    status = models.CharField('Status', max_length=30)

    registration = models.ForeignKey(
        'registrations.Registration',
        on_delete=models.CASCADE,
        related_name='registration_carts',
        verbose_name='Matrícula'
    )

    discipline = models.ForeignKey(
        'disciplines.Discipline',
        on_delete=models.CASCADE,
        related_name='registration_carts',
        verbose_name='Disciplina'
    )

    teacher = models.ForeignKey(
        'teachers.Teacher',
        on_delete=models.CASCADE,
        related_name='registration_carts',
        verbose_name='Professor'
    )

