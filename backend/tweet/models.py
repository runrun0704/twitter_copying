from django.db import models
import uuid
from tag.models import Tag

# Create your models here.
class Tweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=30)
    body = models.TextField()
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tweet_users')
    good_count = models.IntegerField(null=True, default=0)
    tags = models.ManyToManyField(Tag, through="TweetTag", null=True)

SEX = (
    ('M', 'Mail'),
    ('F', 'Femail')
)
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    domain = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=SEX)
    age = models.IntegerField()
    status = models.CharField(max_length=10)


class TweetTag(models.Model):
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
