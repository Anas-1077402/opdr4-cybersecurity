from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from datetime import date
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password

class Toezichthouders(models.Model):
    ervaringsdeskundige = models.IntegerField(blank=True, null=True)
    voornaam_1 = models.TextField()
    achternaam_1 = models.TextField()
    telefoonnummer_1 = models.TextField()
    voornaam_2 = models.TextField(blank=True, null=True)
    achternaam_2 = models.TextField(blank=True, null=True)
    telefoonnummer_2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Toezichthouders"


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    geslacht = models.CharField(
        max_length=10, choices=[("M", "Man"), ("V", "Vrouw"), ("0", "Anders")]
    )
    email = models.EmailField()
    telefoonnummer = models.CharField(max_length=100)
    geboortedatum = models.DateField()
    gebruikte_hulpmiddelen = models.TextField(max_length=200)
    bijzonderheden = models.TextField(max_length=100, default="", blank=True)
    beschikbaar_vanaf = models.DateTimeField()
    beschikbaar_tot = models.DateTimeField()
    bijzonderheden_beschikbaarheid = models.TextField(max_length=100, blank=True)
    username = models.CharField(max_length=100, unique=True)
    voorkeur_benadering = models.CharField(max_length=20)
    status = models.CharField(max_length=10, default=1)
    opmerking_verwijderd = models.TextField(blank=True, null=True)
    datum_goedgekeurd = models.DateTimeField(blank=True, null=True)
    goedgekeurd_door = models.CharField(max_length=100, null=True)

    # Custom field for salt (if you want to implement your own salting)
    custom_salt = models.CharField(max_length=32, blank=True, null=True)
    
    # user permission
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        related_name="user_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        related_name="user_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )

    def age(self):
        date_today = date.today()
        leeftijd = (
            date_today.year
            - self.geboortedatum.year
            - (
                (date_today.month, date_today.day)
                < (self.geboortedatum.month, self.geboortedatum.day)
            )
        )
        return leeftijd

    def set_custom_password(self, raw_password):
        self.custom_salt = get_random_string(32)
        
        self.password = make_password(raw_password, salt=self.custom_salt)
    
    def check_password(self, raw_password):
        return super().check_password(raw_password)
