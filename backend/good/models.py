from django.db import models

import uuid

from tweet.models import Tweet, User
from comment.models import Comment

# Create your models here.
class Good(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='good_users')
    is_pushed = models.BooleanField(default=False)

class GoodTweet(models.Model):
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='goods_tweets')
    good_id = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='tweets_goods')

class GoodComment(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='goods_comments')
    good_id = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='comments_goods')
