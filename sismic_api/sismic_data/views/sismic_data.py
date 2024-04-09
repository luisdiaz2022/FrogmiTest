"""Sismic_data views."""

# Django REST Framework
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import action

# Models
from sismic_api.sismic_data.models import Feature

# Serializers
from sismic_api.sismic_data.serializers import FeatureSerializer

# Utils
from sismic_api.sismic_data.utils import get_sismic_data

class FeatureListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    
    """Feature view set."""

    def list(self, request, *args, **kwargs):
        sismic_data = get_sismic_data()
        if sismic_data:
            for feature in sismic_data:
                # Send the Feature data to serializer before saving it to the database
                serializer = FeatureSerializer(data={
                    'external_id': Feature['id'],
                    'magnitude': Feature['properties']['mag'],
                    'place': Feature['properties']['place'],
                    'time': Feature['properties']['time'],
                    'tsunami': Feature['properties']['tsunami'],
                    'mag_type': Feature['properties']['magType'],
                    'title': Feature['properties']['title'],
                    'longitude': Feature['geometry']['coordinates'][0],
                    'latitude': Feature['geometry']['coordinates'][1]
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