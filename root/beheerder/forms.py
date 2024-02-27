from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistratieFormulier(UserCreationForm):
    functie = forms.CharField(max_length=100, help_text='Wat is je functie')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'functie')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
