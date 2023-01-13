from django.db import models
import uuid
from tweet.models import Tweet,User

# Create your models here.
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_users')
    parent_id = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweets')
    good_count = models.IntegerField(null=True, default=0)
