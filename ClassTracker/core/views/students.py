from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect

from core.models import Classroom, Student
from core.forms import *


def students_list(request):
    pass

def create_students(request):
    if request.method == 'GET':
        form = StudentChangeForm()
        return render(request, 'students-new.html', {'data': {'form': form}})

    elif request.method == 'POST':
        form = StudentChangeForm(request.POST)
        if form.is_valid():
            student = form.save()
            print(student)
            return render(request, 'students-by-id.html', {'data': {'student': student}})
        return render(request, 'students-new.html', {'data': {'form': form}})


        
def students_by_id(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':

            try:
                student = Student.objects.get(id=id)
            except:
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
                pass
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
            