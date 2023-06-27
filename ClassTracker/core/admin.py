from django.contrib import admin
from core.models import Teacher, Student, Classroom, School

from django.contrib.auth.admin import UserAdmin

from core.forms import *

class TeacherAdmin(UserAdmin):
    model = Teacher
    list_display = ['phone_number', 'subject_name']


admin.site.register(School)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Classroom)
admin.site.register(Student)
