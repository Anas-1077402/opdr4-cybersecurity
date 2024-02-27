from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'postcode', 'geslacht','email', 'telefoonnummer', 'geboortedatum', 'gebruikte_hulpmiddelen',
                  'bijzonderheden', 'bijzonderheden_beschikbaarheid', 'username',)
