from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect

from core.models import Classroom, Student
from core.forms import *

from core.utils.email import notify_student


def students_list(request):
    if request.method == 'GET':
        try:
            students = Student.objects.all()
        except:
            return render(request, 'students.html', {'data': None})
        
        return render(request, 'students.html', {'data': {'students': students}})


def create_students(request):
    if request.method == 'GET':
        form = StudentChangeForm()
        return render(request, 'students-new.html', {'data': {'form': form}})

    elif request.method == 'POST':
        form = StudentChangeForm(request.POST)
        if form.is_valid():
            student = form.save()
            
            notify_student(student, subject='Welcome Letter', body="Welcome to our class!")

            return render(request, 'students-by-id.html', {'data': {'student': student}})
        return render(request, 'students-new.html', {'data': {'form': form}})


        
def students_by_id(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':

            try:
                student = Student.objects.get(id=id)
            except:
        # todo handle no object
                pass

            return render(request, 'students-by-id.html', {'data': {'student': student}})
    else:
        return redirect('log-in')
# <!-- <p><a href="{% url 'delete-student-by-id' data.student.id %}">Delete this student</a></p> -->

def edit_students_by_id(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                student = Student.objects.get(id=id)
            except:
                pass
        # todo handle no object

            form = StudentChangeForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                print(student)
                return render(request, 'students-by-id.html', {'data': {'student': student}})

            return render(request, 'edit-students-by-id.html', {'data': {'form': form, 'student': student}})

        elif request.method == 'GET':
            try:
                student = Student.objects.get(id=id)
            except:
                return render(request, 'edit-students-by-id.html', {'data': None})
        # todo handle no object

            form = StudentChangeForm(instance=student)

            return render(request, 'edit-students-by-id.html', {'data': {'form': form, 'student': student}})
    else:
        return redirect('log-in')
            
            
def delete_students_by_id(request, id):
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return redirect('classrooms-by-id', student.classroom.id)
        except:
            pass

        return render(request, 'students-by-id.html', {'data': {'student': student}})

    else:
        return redirect('log-in')
            