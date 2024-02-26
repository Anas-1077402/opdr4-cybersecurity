from rest_framework import serializers
from .models_test import Organisatie, Onderzoeken


class OrganisatieSerializer(serializers.Serializer):
    organistatie_id = serializers.IntegerField(read_only=True)
    naam = serializers.CharField(max_length=255)
    website = serializers.URLField()
    beschrijving = serializers.CharField(max_length=500)
    contactpersoon = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    telefoonnummer = serializers.CharField(max_length=64)
    overige_details = serializers.CharField(max_length=500)


    # onderzoeks_id = serializers.AutoField(primary_key=True)
    # organisatie = serializers.ForeignKey('Organisaties', models.DO_NOTHING)
    # status = serializers.IntegerField()
    # titel = serializers.TextField()
    # omschrijving = serializers.TextField()
    # datum_vanaf = serializers.DateTimeField()
    # datum_tot = serializers.DateTimeField()
    # soort_onderzoek = serializers.IntegerField()
    # locatie = serializers.TextField(blank=True, null=True)
    # met_beloning = serializers.IntegerField()
    # beloning = serializers.TextField(blank=True, null=True)
    # doelgroep_leeftijd_van = serializers.IntegerField()
    # doelgroep_leeftijd_tot = serializers.IntegerField()
    # contact_opgenomen = serializers.IntegerField()
    # opmerkingen_beheerder = serializers.IntegerField(blank=True, null=True)
    # type_onderzoek = serializers.ForeignKey('TypeOnderzoek', serializers.DO_NOTHING, db_column='type_onderzoek')

    class Meta:
        managed = False
        db_table = 'Onderzoeken'


    def create(self, validated_data):
        return Organisatie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.naam = validated_data.get('naam', instance.naam)
        instance.website = validated_data.get('website', instance.website)
        instance.beschrijving = validated_data.get('beschrijving', instance.beschrijving)
        instance.contactpersoon = validated_data.get('contactpersoon', instance.contactpersoon)
        instance.email = validated_data.get('email', instance.email)
        instance.telefoonnummer = validated_data.get('telefoonnummer', instance.telefoonnummer)
        instance.overige_details = validated_data.get('overige_details', instance.overige_details)
        instance.save()
        return instance


class OnderzoekenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onderzoeken
        fields = [
            'id',
            'organisatie_id',
            'titel',
            'status',
            'avili',
            'datef',
            'datet',
            'location',
            'met_belonging'
        ]
