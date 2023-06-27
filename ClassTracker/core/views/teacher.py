from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from core.forms import TeacherSignUpForm, TeacherLogInForm

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

def sign_up(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            login(request, teacher)
            return redirect('home')
    else:
        form = TeacherSignUpForm()   
    return render(request, 'sign-up.html', {'form': form})


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = TeacherLogInForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            teacher = authenticate(phone_number=phone_number, password=password)
            print(teacher)
            if teacher:
                login(request, teacher)  
                return redirect('home')
            else:
                error = True
    else:
        form = TeacherLogInForm()

    return render(request, 'log-in.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect('home')
