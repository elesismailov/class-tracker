from django.db import models

class Classroom(models.Model):

    name = models.CharField(max_length=50, blank=False)

    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    school = models.ForeignKey('School', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.teacher.name()

