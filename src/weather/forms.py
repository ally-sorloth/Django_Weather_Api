from django import forms
from django.forms import fields
from .models import City

class CityForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'City Name'}))
    class Meta:
        model = City
        fields = ("name", )