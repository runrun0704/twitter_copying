from rest_framework import routers

from .views import TagViewSet

router = routers.DefaultRouter()

router.register(r'tags', TagViewSet)
