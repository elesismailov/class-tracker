from django import forms
from core.models import Classroom

class ClassroomCreateForm(forms.ModelForm):

    class Meta:
        model = Classroom
        exclude = ['id']

class ClassroomUpdateForm(forms.ModelForm):

    class Meta:
        model = Classroom
        exclude = ['id']

class EmailClassroomForm(forms.Form):
    subject = forms.CharField(max_length=200)
    body    = forms.CharField(widget=forms.Textarea)