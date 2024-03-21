from rest_framework import serializers
from .models import Organisaties, Onderzoeken
from ervaringsdeskundige.models import User


class OrganisatieSerializer(serializers.Serializer):
    organistatie_id = serializers.IntegerField(read_only=True)
    naam = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    kvk = serializers.CharField(max_length=255, allow_blank=True, allow_null=True, source='KVK')
    website = serializers.URLField(allow_blank=True, allow_null=True)
    beschrijving = serializers.CharField(max_length=500, allow_blank=True, allow_null=True)
    contact_persoon = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    email = serializers.EmailField(allow_blank=True, allow_null=True)
    telefoonnummer = serializers.CharField(max_length=64, allow_blank=True, allow_null=True)
    api_key = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    status = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    type = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)

    class Meta:
        managed = False
        db_table = 'Onderzoeken'


    def create(self, validated_data):
        return Organisaties.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.naam = validated_data.get('naam', instance.naam)
        instance.kvk = validated_data.get('kvk', instance.kvk)
        instance.website = validated_data.get('website', instance.website)
        instance.beschrijving = validated_data.get('beschrijving', instance.beschrijving)
        instance.contact_persoon = validated_data.get('contactpersoon', instance.contact_persoon)
        instance.email = validated_data.get('email', instance.email)
        instance.telefoonnummer = validated_data.get('telefoonnummer', instance.telefoonnummer)
        instance.api_key = validated_data.get('api_key', instance.api_key)
        instance.status = validated_data.get('status', instance.status)
        instance.type = validated_data.get('type', instance.type)

        instance.save()
        return instance


class OnderzoekenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onderzoeken
        fields = [
            'onderzoeks_id',
            'organisatie_id',
            'status',
            'titel',
            'omschrijving',
            'datum_vanaf',
            'datum_tot',
            'soort_onderzoek',
            'locatie',
            'met_beloning',
            'beloning',
            'doelgroep_leeftijd_van',
            'doelgroep_leeftijd_tot',
            'contact_opgenomen',
            'opmerkingen_beheerder',
        ]


class ExperienceExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
                'postcode',
                'geslacht',
                'gebruikte_hulpmiddelen',
                'bijzonderheden',
                'voorkeur_benadering',
                'geboortedatum',
                'telefoonnummer',
                'bijzonderheden_beschikbaarheid',
                'status',
        ]
# 'password',
# 'last_login',
# 'is_superuser',
# 'is_staff',
# 'is_active',
# 'date_joined',
# 'datum_goedgekeurd',
# 'goedegekeurd_door',
