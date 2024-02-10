from django.db import models
from django.contrib.auth.models import AbstractUser


class Ervaringsdeskundige(AbstractUser):
    email = models.EmailField()
    wachtwoord = models.CharField(('password'), max_length=128, help_text=("Gebruik een geldige, en sterke wachtwoord"))
    gebruikersnaam = models.CharField(max_length=100)
    voornaam = models.CharField(max_length=100)
    achternaam = models.CharField(max_length=100)
    #hier ga ik nog meer models toevoegen