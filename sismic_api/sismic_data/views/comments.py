"""Comments View."""

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets  import ViewSet
from rest_framework.decorators import action

# Models
from sismic_api.sismic_data.models import Feature, Comment

# Serializers
from sismic_api.sismic_data.serializers import CommentSerializer

class CreateCommentView(ViewSet):
    def create(self, request, feature_id):
        try:
            feature = Feature.objects.get(pk=feature_id)
        except Feature.DoesNotExist:
            return Response({"error": "Feature does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            body = serializer.validated_data.get('body')
            if body:
                comment = Comment.objects.create(feature=feature, body=body)
                return Response({"message": "Comment created successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Body must not be empty."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)