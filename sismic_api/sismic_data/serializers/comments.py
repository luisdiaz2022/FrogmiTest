"""Comments Serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from sismic_api.sismic_data.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'created_at']