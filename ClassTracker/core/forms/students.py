from django import forms
from core.models import Student

class EmailStudentForm(forms.Form):
    subject = forms.CharField(max_length=200)
    body    = forms.CharField(widget=forms.Textarea)

class StudentChangeForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['id']