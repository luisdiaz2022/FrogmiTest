"""Sismic_data views."""

# Utilities
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

# Django REST Framework
from rest_framework.response import Response
from rest_framework import viewsets, mixins

# Models
from sismic_api.sismic_data.models import Feature

# Serializers
from sismic_api.sismic_data.serializers import FeatureSerializer

# Api
from sismic_api.sismic_data.api import get_sismic_data

class FeatureListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    
    """Feature view set."""

    def save_features(self, request, *args, **kwargs):
        """ In this method we are getting the data from GeoJson,
        and saving it on our BD
        """

        sismic_data = get_sismic_data()
        if sismic_data: # cambiar a try catch -- debemos mostrar cual error esta pasando
            for feature in sismic_data: # Opcional Bulk_create permite trabajar performante con grandes datos

                # Convert the time provided by GeopJson into a DateTime field
                timestamp = feature['properties']['time'] / 1000  # Convertir milisegundos a segundos
                formatted_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

                # Take the decimal provided by GeopJson and round them up into the max amount allowed
                longitude = Decimal(feature['geometry']['coordinates'][0]).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP) #get ATTR revisar para obtener el valor del diccionario
                latitude = Decimal(feature['geometry']['coordinates'][1]).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP) #ceil function recommend by cabrera to round up
                magnitude = Decimal(feature['properties']['mag'],).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)

                # Verify if the Feature already exists # mover a serializer
                if Feature.objects.filter( # update or create method - mas performante
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
        """Get all the features."""
        queryset = Feature.objects.all()
        return queryset