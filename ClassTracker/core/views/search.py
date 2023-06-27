
from django.urls import reverse_lazy
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, redirect

from core.models import Classroom, Student
from core.forms import *

from core.utils.email import notify_email


def search(request):
    if request.method == 'GET':
        return render(request, 'search.html', {'data': { }})

    elif request.method == 'POST':
        q = request.POST['query']
        first = Student.objects.filter(first_name__icontains=q)
        second = Student.objects.filter(second_name__icontains=q)
        emails = Student.objects.filter(email__icontains=q)

        final = set(list(first) + list(second) + list(emails))

        #### _____ This is a full body text search
        # final = Student.objects.annotate(
        #     search=SearchVector("first_name", "second_name"),
        # ).filter(search=q)
        # print(final)

        if len(final):
            return render(request, 'search.html', {'data': { 'students': final, 'q': q}})

        return render(request, 'search.html', {'data': { 'message': 'No match so far :(', 'students': final, 'q': q}})