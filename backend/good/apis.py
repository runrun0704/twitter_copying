from rest_framework import routers

from .views import GoodTweetViewSet, GoodCommentViewSet

router = routers.DefaultRouter()

router.register(r'goodtweet', GoodTweetViewSet)
router.register(r'goodcomment', GoodCommentViewSet)
