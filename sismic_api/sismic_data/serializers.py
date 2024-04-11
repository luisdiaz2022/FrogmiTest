"""Sismic_data Serializer"""

# Utilities
from decimal import Decimal, ROUND_HALF_UP
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers

# Model
from .models import Feature

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = [
            'id', 
            'external_id', 
            'magnitude', 
            'place', 
            'time', 
            'tsunami', 
            'mag_type', 
            'title', 
            'longitude', 
            'latitude'
        ]

    def create(self, validated_data):

        # Convert the time provided by GeopJson into a DateTime field
        timestamp = validated_data['time'] / 1000  # Convertir milisegundos a segundos
        formatted_time = timezone.datetime.fromtimestamp(timestamp, tz=timezone.utc)
        validated_data['time'] = formatted_time

        # Take the decimal provided by GeopJson and round them up into the max amount allowed
        validated_data['longitude'] = Decimal(validated_data['longitude']).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
        validated_data['latitude'] = Decimal(validated_data['latitude']).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
        validated_data['magnitude'] = Decimal(validated_data['magnitude']).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)

        # Verify if the Feature already exists # mover a serializer
        feature, created = Feature.objects.update_or_create(
            external_id=validated_data['external_id'],
            defaults=validated_data
        )

        return feature