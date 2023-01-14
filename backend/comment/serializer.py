from rest_framework import serializers

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id', 'body', 'user_id', 'parent_id', 'good_count'
        )
