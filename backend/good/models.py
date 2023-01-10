from django.db import models
import uuid
from tweet.models import User

# Create your models here.
class Good(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='good_users')
    is_pushed = models.BooleanField(default=False)

class GoodParent(models.Model):
    parend_id = models.CharField(max_length=50)
    good_id = models.ForeignKey('Good', on_delete=models.CASCADE, related_name='goods')
