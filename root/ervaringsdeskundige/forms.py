from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Ervaringsdeskundige


class RegisterForm(UserCreationForm):
    class Meta:
        model = Ervaringsdeskundige
        fields = ('first_name', 'last_name', 'postcode', 'geslacht','email', 'telefoonnummer', 'geboortedatum', 'gebruikte_hulpmiddelen',
                  'bijzonderheden', 'bijzonderheden_beschikbaarheid', 'username',)
