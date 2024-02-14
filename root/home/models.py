from django.db import models
# import hashlib


# class gebruiker():
class Organisatie(models.Model):
    naam = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    beschrijving = models.CharField(max_length=500, blank=True)
    contactpersoon = models.CharField(max_length=255)
    email = models.EmailField()
    telefoonnummer = models.CharField(max_length=64)
    overige_details = models.CharField(max_length=500)


class Onderzoeken(models.Model):
    organisatie_id = models.ForeignKey(Organisatie, on_delete=models.CASCADE)
    titel = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    avili = models.BooleanField(default=True)
    datef = models.DateField(blank=True, auto_now=True)
    datet = models.DateField(blank=True, auto_now=True)
    location = models.CharField(max_length=255, blank=True, default='')
    met_belonging = models.BooleanField(default=False)
