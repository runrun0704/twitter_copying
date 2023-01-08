from django.contrib import admin
from .models import Tweet,User,TweetTag

# Register your models here.
admin.site.register(Tweet)
admin.site.register(User)
admin.site.register(TweetTag)
