# forms.py
from django import forms

class SubjectForm(forms.Form):
    subject1 = forms.CharField(max_length=100)
    subject2 = forms.CharField(max_length=100)
    subject3 = forms.CharField(max_length=100)
    subject4 = forms.CharField(max_length=100)
    subject5 = forms.CharField(max_length=100)
