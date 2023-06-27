
from django.urls import reverse_lazy

from django.shortcuts import render, redirect

from core.models import Classroom, Student
from core.forms import *

from core.utils.email import notify_email


def search(request):
    if request.method == 'GET':
        return render(request, 'search.html', {'data': { }})

    elif request.method == 'POST':
        form = StudentChangeForm(request.POST)
        if form.is_valid():
            student = form.save()
            
            notify_email([student.email], subject='Welcome Letter', body="Welcome to our class!")

            return render(request, 'students-by-id.html', {'data': {'student': student}})
        return render(request, 'students-new.html', {'data': {'form': form}})
