from django.db import models
import django.dispatch

class Student(models.Model):

    first_name  = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=20, blank=False)
    email       = models.EmailField(unique=True, blank=False)
    birth_date  = models.DateField(blank=False)
    gender      = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M')
    classroom   = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    address     = models.CharField(max_length=200)

    def name(self):
        return self.first_name + ' ' + self.second_name

    def __str__(self):
        return self.name() + ' ' + self.email

    def send_signal_created(self):

        student_created = django.dispatch.Signal()
        student_created.send(sender=self.__class__)

    #### ---------- This is how you will subscribe to this signal
    # @receiver(pre_save, sender=Student)
    # def my_handler(sender, **kwargs):
        # pass

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:
            self.send_signal_created()

        # Everything happenning below this runs every update

        return super(Student, self).save(*args, **kwargs)




