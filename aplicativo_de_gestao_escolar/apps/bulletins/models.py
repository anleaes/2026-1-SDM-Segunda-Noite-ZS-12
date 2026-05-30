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

    class Meta:
        verbose_name = 'Bulletin'
        verbose_name_plural = 'Bulletins'
        ordering = ['id']

    def __str__(self):
        return f'Bulletin - {self.student} ({self.school_year} / Sem {self.semester})'
