from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect

from core.models import *
from core.forms import *

def classrooms_list(request):
    if request.method == 'GET':
        try:
            classrooms = Classroom.objects.filter(teacher=request.user)
            print(list(classrooms))
        except:
            return render(request, 'classrooms-all.html', {'data': None})
        
        return render(request, 'classrooms-all.html', {'data': list(classrooms)})

def create_classrooms(request):
    if request.method == 'GET':
        form = ClassroomCreateForm()
        return render(request, 'classroom-new.html', {'data': {'form': form}})

    elif request.method == 'POST':
        form = ClassroomCreateForm(request.POST)
        if form.is_valid():
            classroom = form.save()
            print(classroom)
            return render(request, 'classroom-by-id.html', {'data': {'classroom': classroom}})
        return render(request, 'classroom-new.html', {'data': {'form': form}})
        

def edit_classrooms_by_id(request, id):
    if request.method == 'POST':
        try:
            classroom = Classroom.objects.get(id=id)
        except:
            return render(request, 'edit-classrooms-by-id.html', {'data': None})
        # todo handle no object

        form = ClassroomUpdateForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            print(classroom)
            return render(request, 'classrooms-by-id.html', {'data': {'classroom': classroom}})

        return render(request, 'edit-classrooms-by-id.html', {'data': {'form': form, 'classroom': classroom}})

    elif request.method == 'GET':
        try:
            classroom = Classroom.objects.get(id=id)
        except:
            return render(request, 'edit-classrooms-by-id.html', {'data': None})
        # todo handle no object

        form = ClassroomUpdateForm(instance=classroom)

        return render(request, 'edit-classrooms-by-id.html', {'data': {'form': form, 'classroom': classroom}})


def delete_classrooms_by_id(request, id):
    pass

def classrooms_by_id(request, id):
    print(id)
    if request.method == 'GET':
        if request.user.is_authenticated:

            try:
                c = Classroom.objects.get(id=id)
            except:
                return render(request, 'classroom-by-id.html', {'data': None})
            try:
                s = Student.objects.filter(classroom=c)
            except:
                return render(request, 'classroom-by-id.html', {'data': {'classroom': c, 'students': None}})
            
            return render(request, 'classroom-by-id.html', {'data': {'classroom': c, 'students': s}})
        else:
            return render(request, 'classroom-by-id.html', {'data': None})
