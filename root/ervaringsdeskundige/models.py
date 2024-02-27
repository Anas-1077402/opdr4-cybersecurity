from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from main.models import Toezichthouders
from beheerder.models import Beheerders



class Ervaringsdeskundige(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    geslacht = models.CharField(max_length=10, choices=[('M','Man'),('V', 'Vrouw'), ('0', 'Anders')])
    email = models.EmailField()
    telefoonnummer = models.CharField(max_length=100)
    geboortedatum = models.DateField()
    gebruikte_hulpmiddelen = models.TextField(max_length=200)
    bijzonderheden = models.TextField(max_length=100, default='', blank=True)
    bijzonderheden_beschikbaarheid = models.TextField(max_length=100, blank=True)
    username = models.CharField(max_length=100)
    voorkeur_benadering = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    toezichthouder = models.ForeignKey(
        Toezichthouders,
        on_delete=models.CASCADE,
        related_name='ervaringsdeskundige_toezichthouders'
    )
    datum_goedgekeurd = models.DateTimeField(blank=True, null=True)
    goedegekeurd_door = models.ForeignKey(Beheerders, models.DO_NOTHING, db_column='goedegekeurd_door', blank=True, null=True)
    #userpermission
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        related_name='ervaringsdeskundige_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='ervaringsdeskundige',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        related_name='ervaringsdeskundige_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='ervaringsdeskundige',
    )


class BeperkingenErvaringsdeskundigen(models.Model):
    beperking_id = models.IntegerField()
    ervaringsdeskundigen_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Beperkingen_ervaringsdeskundigen'


class BeperkingenOnderzoeken(models.Model):
    onderzoeks_id = models.IntegerField()
    beperking_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Beperkingen_onderzoeken'