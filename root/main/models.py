# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from ervaringsdeskundige.models import User



class Beperkingen(models.Model):
    omschrijving = models.TextField()
    soort = models.TextField()

    class Meta:
        managed = False
        db_table = 'Beperkingen'


class Deelnames(models.Model):
    onderzoeks = models.ForeignKey('Onderzoeken', models.DO_NOTHING)
    ervaringsdeskundige = models.ForeignKey(User, models.DO_NOTHING, )
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Deelnames'


class Organisaties(models.Model):
    organisatie_id = models.AutoField(primary_key=True, blank=True)
    naam = models.TextField(blank=True, null=True)
    kvk = models.TextField(db_column='KVK', blank=True, null=True)  # Field name made lowercase.
    website = models.TextField(blank=True, null=True)
    beschrijving = models.TextField(blank=True, null=True)
    contact_persoon = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    telefoonnummer = models.IntegerField(blank=True, null=True)
    api_key = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Organisaties'


class Onderzoeken(models.Model):
    onderzoeks_id = models.AutoField(primary_key=True)
    organisatie = models.ForeignKey('Organisaties', models.DO_NOTHING)
    status = models.IntegerField()
    titel = models.TextField()
    omschrijving = models.TextField()
    datum_vanaf = models.DateTimeField()
    datum_tot = models.DateTimeField()
    soort_onderzoek = models.IntegerField()
    locatie = models.TextField(blank=True, null=True)
    met_beloning = models.IntegerField()
    beloning = models.TextField(blank=True, null=True)
    doelgroep_leeftijd_van = models.IntegerField()
    doelgroep_leeftijd_tot = models.IntegerField()
    contact_opgenomen = models.IntegerField()
    opmerkingen_beheerder = models.IntegerField(blank=True, null=True)
    type_onderzoek = models.ForeignKey('TypeOnderzoek', models.DO_NOTHING, db_column='type_onderzoek')

    class Meta:
        managed = False
        db_table = 'Onderzoeken'



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
        db_table = 'Toezichthouders'


class TypeOnderzoek(models.Model):
    telefonisch = models.BooleanField(blank=True, null=True)
    internet = models.BooleanField(blank=True, null=True)
    locatie = models.BooleanField(blank=True, null=True)
    onderzoeks = models.ForeignKey(Onderzoeken, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Type_onderzoek'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)



class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class BeperkingenErvaringsdeskundigen(models.Model):
    beperking_id = models.IntegerField()
    ervaringsdeskundigen_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Beperkingen_ervaringsdeskundigen'



# class ErvaringsdeskundigeUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#     email = models.CharField(max_length=254)
#     postcode = models.CharField(max_length=10)
#     geslacht = models.CharField(max_length=10)
#     gebruikte_hulpmiddelen = models.TextField()
#     bijzonderheden = models.TextField()
#     voorkeur_benadering = models.CharField(max_length=20)
#     geboortedatum = models.DateField()
#     telefoonnummer = models.CharField(max_length=100)
#     beschikbaar_vanaf = models.DateTimeField(blank=True, null=True)
#     beschikbaar_tot = models.DateTimeField(blank=True, null=True)
#     bijzonderheden_beschikbaarheid = models.TextField()
#     datum_goedgekeurd = models.DateTimeField(blank=True, null=True)
#     goedegekeurd_door = models.ForeignKey(BeheerderBeheerders, models.DO_NOTHING, db_column='goedegekeurd_door', blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     opmerking_verwijderd = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'ervaringsdeskundige_user'



# class ErvaringsdeskundigeErvaringsdeskundigeGroups(models.Model):
#     ervaringsdeskundige = models.ForeignKey(ErvaringsdeskundigeErvaringsdeskundige, models.DO_NOTHING)
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'ervaringsdeskundige_ervaringsdeskundige_groups'
#         unique_together = (('ervaringsdeskundige', 'group'),)


# class ErvaringsdeskundigeErvaringsdeskundigeUserPermissions(models.Model):
#     ervaringsdeskundige = models.ForeignKey(ErvaringsdeskundigeErvaringsdeskundige, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'ervaringsdeskundige_ervaringsdeskundige_user_permissions'
#         unique_together = (('ervaringsdeskundige', 'permission'),)


# class HomeCustomuser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'home_customuser'


# class HomeCustomuserGroups(models.Model):
#     customuser = models.ForeignKey(HomeCustomuser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'home_customuser_groups'
#         unique_together = (('customuser', 'group'),)


# class HomeCustomuserUserPermissions(models.Model):
#     customuser = models.ForeignKey(HomeCustomuser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'home_customuser_user_permissions'
#         unique_together = (('customuser', 'permission'),)
