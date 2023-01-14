from django.db import models

import uuid

from tweet.models import Tweet, User
from comment.models import Comment

# Create your models here.
class GoodTweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goodtweet_users', blank=True, null=True)
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='goods_tweets')

class GoodComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goodcomment_users', blank=True, null=True)
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='goods_comments')
