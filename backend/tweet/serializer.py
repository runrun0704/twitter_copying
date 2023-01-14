from rest_framework import serializers

from .models import Tweet, User, TweetTag

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = (
            'id', 'title', 'body', 'user_id', 'good_count', 'tags'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'name', 'domain', 'password', 'sex', 'age', 'status'
        )

class TweetTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetTag
        fields = ('tweet_id', 'tag_id')
