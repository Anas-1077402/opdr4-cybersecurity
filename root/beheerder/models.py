# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # hier later extra vakken toevoegen...
    functie = models.CharField(max_length=100, blank=True, null=True)

