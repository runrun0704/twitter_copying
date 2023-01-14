from rest_framework import routers

from .views import GoodViewSet, GoodTweetViewSet, GoodCommentViewSet

router = routers.DefaultRouter()

router.register(r'goods', GoodViewSet)
router.register(r'goodtweet', GoodTweetViewSet)
router.register(r'goodcomment', GoodCommentViewSet)
