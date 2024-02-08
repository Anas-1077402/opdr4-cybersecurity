from django.db import models
# import hashlib


# class gebruiker():
class Organistatie(models.Model):
    naam = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    beschrijving = models.CharField(max_length=255, blank=True)
    contactpersoon = models.CharField(max_length=255)
    email = models.EmailField()
    telefoonnummer = models.CharField(max_length=64)
    overige_details = models.CharField(max_length=255)
