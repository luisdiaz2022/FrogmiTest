"""Sismic_data views."""

# Django REST Framework
from rest_framework.response import Response
from rest_framework import viewsets, mixins

# Models
from sismic_api.sismic_data.models.features import Feature

# Serializers
from sismic_api.sismic_data.serializers.features import FeatureSerializer

# Api
from sismic_api.sismic_data.api import get_sismic_data

class FeatureListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    
    """Feature view set."""

    serializer_class = FeatureSerializer

    def save_features(self, request, *args, **kwargs):
        """ In this method we are getting the data from GeoJson,
        and saving it on our BD
        """

        sismic_data = get_sismic_data()
        if sismic_data: # cambiar a try catch -- debemos mostrar cual error esta pasando
            features_to_create = []

            for feature in sismic_data:
                serializer = FeatureSerializer(data={
                    'external_id': feature.get('external_id', ''),
                    'magnitude': feature['properties']['mag'],
                    'place': feature['properties']['place'],
                    'time': feature['properties']['time'],
                    'tsunami': feature['properties']['tsunami'],
                    'mag_type': feature['properties']['magType'],
                    'title': feature['properties']['title'],
                    'longitude': feature['geometry']['coordinates'][0],
                    'latitude': feature['geometry']['coordinates'][1]
                })
                if serializer.is_valid():
                    feature_instance = serializer.save()
                    features_to_create.append(feature_instance)
                else:
                    return Response(serializer.errors, status=400)
                
            Feature.objects.bulk_create(features_to_create)

            return Response({'message': 'Datos sismológicos guardados exitosamente'})
        else:
            return Response({'error': 'No se pudieron obtener los datos sismológicos'}, status=500)
        
    def get_queryset(self):
        """Get all the features."""
        queryset = Feature.objects.all()
        return queryset