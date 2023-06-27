
from django.shortcuts import render, redirect

from core.models import *
from core.forms import *
from core.utils.email import notify_email

def classrooms_list(request):
    if request.method == 'GET':
        try:
            classrooms = Classroom.objects.all()
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
    try:
        classroom = Classroom.objects.get(id=id)
        classroom.delete()
        return redirect('classrooms-all')
    except:
        pass
    return render(request, 'classrooms-by-id.html', {'data': {'classroom': classroom}})

def classrooms_by_id(request, id):
    print(id)
    if request.method == 'GET':
        if request.user.is_authenticated:

            try:
                c = Classroom.objects.get(id=id)
            except:
                return render(request, 'classrooms-by-id.html', {'data': None})
            try:
                s = Student.objects.filter(classroom=c)
            except:
                return render(request, 'classrooms-by-id.html', {'data': {'classroom': c, 'students': None}})
            
            return render(request, 'classrooms-by-id.html', {'data': {'classroom': c, 'students': s}})
        else:
            return render(request, 'classrooms-by-id.html', {'data': None})


def parse_email(e):
    return e['email']
          
def email_classrooms_by_id(request, id):
    if request.method == 'POST':
        try:
            classroom = Classroom.objects.get(id=id)
            students  = Student.objects.filter(classroom=classroom)
            query     = students.values('email')
            emails = map(parse_email, list(query))
            print(list(emails))

        except:
            pass
        # todo handle no object

        notify_email(
            emails,
            subject=request.POST['subject'],
            body=request.POST['body']
            )
        return render(request, 'classrooms-by-id.html', {'data': {'classroom': classroom, 'students': students, 'message': 'Email has been successfully sent!'}})

    elif request.method == 'GET':
        try:
            classroom = Classroom.objects.get(id=id)
        except:
            return render(request, 'classrooms-by-id.html', {'data': None})
    # todo handle no object

        form = EmailClassroomForm()

        return render(request, 'email-classrooms-by-id.html', {'data': {'form': form, 'classroom': classroom}})
 