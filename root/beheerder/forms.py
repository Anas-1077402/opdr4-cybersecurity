from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistratieFormulier(UserCreationForm):
    functie = forms.CharField(max_length=100, help_text='Wat is je functie')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'functie')
