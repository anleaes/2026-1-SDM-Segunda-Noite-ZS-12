from django.db import models


class Bulletins(models.Model):
    school_year = models.IntegerField('School Year')
    semester = models.IntegerField('Semester')
    final_situation = models.CharField('Final Situation', max_length=50)

    student = models.OneToOneField(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='bulletin',
        verbose_name='Student'
    )
