from rest_framework import serializers
from sismic_api.sismic_data.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'created_at']  # Ajusta los campos según sea necesario