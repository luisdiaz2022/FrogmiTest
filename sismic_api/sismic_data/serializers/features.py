"""Sismic_data Serializer"""

# Utilities
from decimal import Decimal, ROUND_HALF_UP
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.utils.timezone import now

# Django REST Framework
from rest_framework import serializers

# Model
from sismic_api.sismic_data.models.features import Feature

class FeatureSerializer(serializers.ModelSerializer):
    external_id = serializers.CharField(
        max_length=255,
        )
    magnitude = serializers.DecimalField(
        max_digits=5, 
        decimal_places=2,
        )
    place = serializers.CharField(max_length=255)
    time = serializers.DateTimeField()
    url = serializers.CharField(max_length=255)
    tsunami = serializers.BooleanField()
    mag_type = serializers.CharField(max_length=10)
    title = serializers.CharField(
        max_length=255, 
        )
    longitude = serializers.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        )
    latitude = serializers.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        )

    class Meta:
        model = Feature
        fields = [
            'id', 
            'external_id', 
            'magnitude', 
            'place', 
            'time',
            'url', 
            'tsunami', 
            'mag_type', 
            'title', 
            'longitude', 
            'latitude'
        ]

    def validate_time(self, value):
        # Convertir el tiempo proporcionado por GeoJSON en un campo DateTime
        print(value)
        timestamp = value['time'] / 1000  # Convertir milisegundos a segundos
        formatted_time = timezone.datetime.strftime(timestamp, "%Y-%m-%d").date()
        value['time'] = formatted_time
        return value['time']
    
    def validate_longitude(self, value):
        print(value)
        return round(float(value), 6)
    
    def validate_latitude(self, value):
        print(value)
        # Tomar el decimal proporcionado por GeoJSON y redondearlo al máximo permitido
        return round(float(value), 6)
    
    def validate_magnitude(self, value):
        print(value)
        # Tomar el decimal proporcionado por GeoJSON y redondearlo al máximo permitido
        return round(float(value), 6)