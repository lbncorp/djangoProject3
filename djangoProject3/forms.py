from .models import Yard, Stat
from django import forms

class StatForm(forms.ModelForm):
    class Meta:
        model = Yard
        fields = ['Receiver']

class StatData(forms.ModelForm):
    class Meta:
        model = Stat
        fields = ['RunningBack1']


