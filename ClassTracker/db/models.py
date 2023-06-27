from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=50)
    # class_ref = models.Reference...
