from django.db import models

class Student(models.Model):

    first_name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=20, blank=False)

    email = models.EmailField(unique=True, blank=False)

    birth_date = models.DateField(blank=False)

    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M')

    classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)

    address = models.CharField(max_length=200)

