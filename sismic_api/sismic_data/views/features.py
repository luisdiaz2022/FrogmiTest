"""Sismic_data views."""

# Django REST Framework
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import status

# Models
from sismic_api.sismic_data.models.features import Feature

# Serializers
from sismic_api.sismic_data.serializers.features import FeatureSerializer

# Api
from sismic_api.sismic_data.api import get_sismic_data


class FeatureListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Feature view set."""

    serializer_class = FeatureSerializer

    def list(self, request, *args, **kwargs):
        """
        Get a list of existing features.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                "message": "Lista de Features recuperada exitosamente",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    
    def create(self, request, *args, **kwargs):
        """
        Create new features from GeoJSON data.
        """
        sismic_data = get_sismic_data()

        if not sismic_data:
            return Response(
                {"error": "No se pudieron obtener los datos sismológicos"}, status=500
            )
        
        for feature in sismic_data:

            if Feature.objects.filter(
                    external_id=feature.get("external_id", ""),
                ).exists():
                    continue
            serializer = FeatureSerializer(
                    data={
                        "external_id": feature.get("external_id", ""),
                        "magnitude": feature["properties"]["mag"],
                        "place": feature["properties"]["place"],
                        "time": feature["properties"]["time"],
                        "url": feature["properties"]["url"],
                        "tsunami": feature["properties"]["tsunami"],
                        "mag_type": feature["properties"]["magType"],
                        "title": feature["properties"]["title"],
                        "longitude": feature["geometry"]["coordinates"][0],
                        "latitude": feature["geometry"]["coordinates"][1],
                    }
                )
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)

            return Response({"message": "Datos sismológicos guardados exitosamente"})

    def get_queryset(self):
        """Get all the features."""
        queryset = Feature.objects.all()
        return queryset