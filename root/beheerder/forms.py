from django import forms
from .models import register

class BeheerderForm(forms.ModelForm):
    class Meta:
        model = register
        fields = ['email', 'username', 'password', 'voornaam', 'achternaam', 'functie', 'status']
        widgets = {
            'password': forms.PasswordInput(),
        }
