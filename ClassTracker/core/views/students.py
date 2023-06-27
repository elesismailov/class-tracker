from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect

def students_list(request):
    if request.method == 'GET':
        return render(request, 'students.html', {'data': 'hello'})
    # if request.method == 'POST':
    #     form = TeacherSignUpForm(request.POST)
    #     if form.is_valid():
    #         teacher = form.save()
    #         login(request, teacher)
    #         return redirect('home')
    # else:
    #     form = TeacherSignUpForm()   
    # return render(request, 'students.html', {'form': form})

