from django import forms
from .models import Ervaringsdeskundige #model nog toevoegen

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Ervaringsdeskundige
        fields = ['e-mail', 'wachtwoord', 'gebruikersnaam', 'voornaam', 'achternaam', 'postcode', 'geslacht', 'gebruikte_hulpmiddelen', 'geboorte_datum', 'bijzonderheden', 'voogd', 'voornaam_voogd', 'achternaam_voogd', 'e-mail_voogd', 'voorkeur_benadering', 'telefonisch_onderzoek', 'internet_onderzoek', 'locatie_onderzoek', 'bijzonderheden_beschikbaarheid']