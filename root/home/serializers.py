from rest_framework import serializers
from .models import Organisatie, Onderzoeken


class OrganisatieSerializer(serializers.Serializer):
    organistatie_id = serializers.IntegerField(read_only=True)
    naam = serializers.CharField(max_length=255)
    website = serializers.URLField()
    beschrijving = serializers.CharField(max_length=500)
    contactpersoon = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    telefoonnummer = serializers.CharField(max_length=64)
    overige_details = serializers.CharField(max_length=500)

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
