from rest_framework import serializers

from .models import Good, GoodTweet, GoodComment

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = (
            'id', 'user_id'
        )

class GoodTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodTweet
        fields = (
            'tweet_id', 'good_id'
        )

class GoodCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodComment
        fields = (
            'comment_id', 'good_id'
        )
