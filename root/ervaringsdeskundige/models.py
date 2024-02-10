from django.contrib.auth.models import AbstractUser
from django.db import models


class Ervaringsdeskundige(AbstractUser):
    email = models.EmailField()
    wachtwoord = models.CharField(('password'), max_length=128, help_text=("Gebruik een geldige, en sterke wachtwoord"))
    gebruikersnaam = models.CharField(max_length=100)
    voornaam = models.CharField(max_length=100)
    achternaam = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    geslacht = models.CharField(max_length=10, choices=[('M','Man'),('V', 'Vrouw'), ('0', 'Anders')])
    geboorte_datum = models.DateField()
    gebruikte_hulpmiddelen = models.CharField(max_length=100)
    bijzonderheden = models.CharField(max_length=100)
    voogd = models.CharField(max_length=100)
    voornaam_voogd = models.CharField(max_length=100)
    email_voogd = models.CharField(max_length=100)
    voorkeurbenadering = models.CharField(max_length=100)
    telefonisch_onderzoek = models.CharField(max_length=100)
    internet_onderzoek = models.CharField(max_length=100)
    locatie_onderzoek = models.CharField(max_length=100)
    bijzonderheden_beschikbaarheid = models.CharField(max_length=100)
    #hier ga ik nog meer velden toevoegen
