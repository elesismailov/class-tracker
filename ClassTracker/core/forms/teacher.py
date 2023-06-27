from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import Teacher

class TeacherSignUpForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Teacher
        fields = ('first_name', 'second_name', 'username', 'email', 'phone_number', 'subject_name')

class TeacherChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Teacher
        fields = ('first_name', 'second_name', 'username', 'email', 'phone_number', 'subject_name')

class TeacherLogInForm(forms.Form):
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
