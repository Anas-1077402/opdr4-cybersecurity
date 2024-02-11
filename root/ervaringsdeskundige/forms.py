from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Ervaringsdeskundige


class RegisterForm(UserCreationForm):
    class Meta:
        model = Ervaringsdeskundige
        fields = ('first_name', 'last_name', 'postcode', 'geslacht','email', 'telefoonnummer', 'geboortedatum', 'type_beperking', 'gebruikte_hulpmiddelen',
                  'bijzonderheden', 'toezichthouder', 'naam_voogd_of_toezichthouder', 'email_voogd_of_toezichthouder', 'telefoonnummer_voogd_of_toezichthouder',
                  'voorkeur_benadering', 'type_onderzoek', 'bijzonderheden_beschikbaarheid', 'username',)

