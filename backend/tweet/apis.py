from rest_framework import routers

from .views import TweetViewSet, UserViewSet, TweetTagViewSet

router = routers.DefaultRouter()

router.register(r'tweets', TweetViewSet)
router.register(r'users', UserViewSet)
router.register(r'tweettags', TweetTagViewSet)
