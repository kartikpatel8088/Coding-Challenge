# forms.py
from django import forms
from .models import *


class HomeForm(forms.ModelForm):
    class Meta:
        model = DataDB
        fields = ['name', 'upload']