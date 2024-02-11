from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Ervaringsdeskundige(AbstractUser):
    email = models.EmailField()
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    geslacht = models.CharField(max_length=10, choices=[('M','Man'),('V', 'Vrouw'), ('0', 'Anders')])
    geboorte_datum = models.DateField()
    gebruikte_hulpmiddelen = models.CharField(max_length=100)
    bijzonderheden = models.CharField(max_length=100, default='', blank=True)
    voogd = models.CharField(max_length=100)
    voornaam_voogd = models.CharField(max_length=100)
    achternaam_voogd = models.CharField(max_length=100)
    email_voogd = models.EmailField(max_length=100)
    VOORKEUR_BENADERING_CHOICES = [('Internet', 'Via Internet'), ('Telefonisch', 'Telefonisch'), ('Locatie', 'Op locatie'),]
    voorkeur_benadering = models.CharField(max_length=20, choices=VOORKEUR_BENADERING_CHOICES, blank=False)
    TYPE_ONDERZOEK_CHOICES = [('Telefonisch Onderzoek', 'Telefonisch Onderzoek'), ('Online Onderzoek', 'Online Onderzoek'), ('Op locatie', 'Onderzoek op locatie'), ]
    type_onderzoek = models.CharField(max_length=100,  default='', choices=TYPE_ONDERZOEK_CHOICES, blank=False)
    bijzonderheden_beschikbaarheid = models.CharField(max_length=100, default='', blank=True)

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
