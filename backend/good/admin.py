from django.contrib import admin
from .models import Good, GoodTweet, GoodComment

# Register your models here.
admin.site.register(Good)
admin.site.register(GoodTweet)
admin.site.register(GoodComment)
