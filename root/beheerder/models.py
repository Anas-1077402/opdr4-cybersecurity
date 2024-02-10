from django.db import models


class register(models.Model):
    beheerder_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    voornaam = models.CharField(max_length=255)
    achternaam = models.CharField(max_length=255)
    functie = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
