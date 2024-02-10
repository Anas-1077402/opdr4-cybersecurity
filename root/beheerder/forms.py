from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistratieFormulier(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Verplicht')
    functie = forms.CharField(max_length=100, help_text='Wat is je functie')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'functie')