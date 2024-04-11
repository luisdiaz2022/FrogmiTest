"""Sismic_data views."""

# Django REST Framework
from rest_framework.response import Response
from rest_framework import viewsets, mixins

# Utilities
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

# Models
from sismic_api.sismic_data.models import Feature

# Serializers
from sismic_api.sismic_data.serializers import FeatureSerializer

# Utils
from sismic_api.sismic_data.api import get_sismic_data

class FeatureListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    
    """Feature view set."""

    def list(self, request, *args, **kwargs):
        sismic_data = get_sismic_data()
        if sismic_data:
            for feature in sismic_data:
                # Convert the time provided by GeopJson into a DateTime field
                timestamp = feature['properties']['time'] / 1000  # Convertir milisegundos a segundos
                formatted_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

                # Take the decimal provided by GeopJson and round them up into the max amount allowed
                longitude = Decimal(feature['geometry']['coordinates'][0]).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
                latitude = Decimal(feature['geometry']['coordinates'][1]).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
                magnitude = Decimal(feature['properties']['mag'],).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)

                # Verify if the Feature already exists
                if Feature.objects.filter(
                    external_id=feature.get('external_id', ''),
                    magnitude=magnitude,
                    place=feature['properties']['place'],
                    time=formatted_time,
                    tsunami=feature['properties']['tsunami'],
                    mag_type=feature['properties']['magType'],
                    title=feature['properties']['title'],
                    longitude=longitude,
                    latitude=latitude
                ).exists():
                    continue  # if already exists, it moves to the next feature

                # Send the Feature data to serializer before saving it to the database
                serializer = FeatureSerializer(data={
                    'external_id': feature.get('external_id', ''),
                    'magnitude': feature['properties']['mag'],
                    'place': feature['properties']['place'],
                    'time': formatted_time,
                    'tsunami': feature['properties']['tsunami'],
                    'mag_type': feature['properties']['magType'],
                    'title': feature['properties']['title'],
                    'longitude': longitude,
                    'latitude': latitude
                })
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=400)
            return Response({'message': 'Datos sismológicos guardados exitosamente'})
        else:
            return Response({'error': 'No se pudieron obtener los datos sismológicos'}, status=500)
        
    def get_queryset(self):
        """Restric list to public-only."""
        queryset = Feature.objects.all()
        return queryset