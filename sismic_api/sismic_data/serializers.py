from rest_framework import serializers
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