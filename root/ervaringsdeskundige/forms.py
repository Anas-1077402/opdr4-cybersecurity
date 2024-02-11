from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Ervaringsdeskundige


class RegisterForm(UserCreationForm):
    class Meta:
        model = Ervaringsdeskundige
        fields = ('email', 'username', 'first_name', 'last_name', 'postcode', 'geslacht', 'gebruikte_hulpmiddelen',
                  'geboorte_datum', 'bijzonderheden', 'voogd', 'voornaam_voogd', 'achternaam_voogd', 'email_voogd',
                  'voorkeur_benadering', 'type_onderzoek', 'bijzonderheden_beschikbaarheid')

