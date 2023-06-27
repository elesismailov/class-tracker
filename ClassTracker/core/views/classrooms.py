from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect

from core.models import Classroom, Student

def classrooms_list(request):
    if request.method == 'GET':
        try:
            classrooms = Classroom.objects.filter(teacher=request.user)
            print(list(classrooms))
        except:
            return render(request, 'classrooms-all.html', {'data': None})
        
        return render(request, 'classrooms-all.html', {'data': list(classrooms)})
# <!-- <a href="{% url 'classrooms' %}">Create New Classroom</a> -->



def classrooms_by_id(request, id):
    print(id)
    if request.method == 'GET':
        if request.user.is_authenticated:

            try:
                c = Classroom.objects.get(id=id)
            except:
                return render(request, 'classroom.html', {'data': None})
            try:
                s = Student.objects.filter(classroom=c)
            except:
                return render(request, 'classroom.html', {'data': {'classroom': c, 'students': None}})
            
            return render(request, 'classroom.html', {'data': {'classroom': c, 'students': s}})
        else:
            return render(request, 'classroom.html', {'data': None})
# <!-- <p><a href="{% url 'edit-classroom-by-id' data.classroom.id %}">Edit this classroom</a></p> -->
# <!-- <p><a href="{% url 'delete-classroom-by-id' data.classroom.id %}">Delete this classroom</a></p> -->
