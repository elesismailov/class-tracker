from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect

from core.models import Classroom, Student

def students_list(request):
    if request.method == 'GET':
        try:
            classrooms = Classroom.objects.get(teacher=request.user)
            print(classrooms)
        except:
            pass
        return render(request, 'students.html', {'classrooms': classrooms}) 

        student_by_id

        
def students_by_id(request, id):
    if request.method == 'GET':
        if request.user.is_authenticated:

            try:
                student = Student.objects.get(id=id)
            except:
                pass

            return render(request, 'students-by-id.html', {'data': {'student': student}})
        else:
            return render(request, 'students-by-id.html', {'data': None})
# <!-- <p><a href="{% url 'edit-student-by-id' data.student.id %}">Edit this student</a></p> -->
# <!-- <p><a href="{% url 'delete-student-by-id' data.student.id %}">Delete this student</a></p> -->
