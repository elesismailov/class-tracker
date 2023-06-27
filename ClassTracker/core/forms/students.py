from django import forms
from core.models import Student

class StudentSignUpForm():
    pass

class StudentChangeForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['id']