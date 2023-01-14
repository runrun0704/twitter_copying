from rest_framework import serializers

from .models import GoodTweet, GoodComment

class GoodTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodTweet
        fields = (
            'id', 'user_id','tweet_id'
        )

class GoodCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodComment
        fields = (
            'id', 'user_id', 'comment_id'
        )
