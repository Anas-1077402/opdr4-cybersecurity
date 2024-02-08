from rest_framework import serializers
from .models import Organistatie


class OrganistatieSerializer(serializers.Serializer):
    organistatie_id = serializers.IntegerField(read_only=True)
    naam = serializers.CharField(max_length=255)
    website = serializers.URLField()
    beschrijving = serializers.CharField()
    contactpersoon = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    telefoonnummer = serializers.CharField(max_length=64)
    overige_details = serializers.CharField()

    def create(self, validated_data):
        return Organistatie.objects.create(validated_data)

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
