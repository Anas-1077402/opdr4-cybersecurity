from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# class Beheerders(AbstractUser):
#     # hier later extra vakken toevoegen...
#     functie = models.CharField(max_length=100, blank=True, null=True)
#     status = models.IntegerField(default=1)


class Beheerders(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"
