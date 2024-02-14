from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Ervaringsdeskundige(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    geslacht = models.CharField(max_length=10, choices=[('M','Man'),('V', 'Vrouw'), ('0', 'Anders')])
    email = models.EmailField()
    telefoonnummer = models.CharField(max_length=100)
    geboortedatum = models.DateField()
    TYPE_BEPERKING_CHOICES = [
        ('auditief', 'Auditieve beperkingen'),
        ('visueel', 'Visuele beperkingen'),
        ('motorisch', 'Motorische / lichamelijke beperkingen'),
        ('cognitief', 'Cognitieve / neurologische beperkingen'),
]
    type_beperking = models.CharField(max_length=100, default='', choices=TYPE_BEPERKING_CHOICES, verbose_name='Type beperking')
    gebruikte_hulpmiddelen = models.TextField(max_length=200)
    bijzonderheden = models.TextField(max_length=100, default='', blank=True)
    toezichthouder = models.BooleanField(default=False, verbose_name='Toezichthouder')
    naam_voogd_of_toezichthouder = models.CharField(max_length=100)
    email_voogd_of_toezichthouder = models.EmailField(max_length=100)
    telefoonnummer_voogd_of_toezichthouder = models.CharField(max_length=100)
    VOORKEUR_BENADERING_CHOICES = [('Internet', 'Via Internet'), ('Telefonisch', 'Telefonisch'), ('Locatie', 'Op locatie'),]
    voorkeur_benadering = models.CharField(max_length=20, choices=VOORKEUR_BENADERING_CHOICES, blank=False)
    TYPE_ONDERZOEK_CHOICES = [('Telefonisch Onderzoek', 'Telefonisch Onderzoek'), ('Online Onderzoek', 'Online Onderzoek'), ('Op locatie', 'Onderzoek op locatie'), ]
    type_onderzoek = models.CharField(max_length=100,  default='', choices=TYPE_ONDERZOEK_CHOICES, blank=False)
    bijzonderheden_beschikbaarheid = models.TextField(max_length=100, blank=True)
    username = models.CharField(max_length=100)
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
