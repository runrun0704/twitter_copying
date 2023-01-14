from django.contrib import admin
from django.urls import path, include

from tweet.apis import router as tweet_api_router
from tag.apis import router as tag_api_router
from comment.apis import router as comment_api_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(tweet_api_router.urls)),
    path('api/tag/', include(tag_api_router.urls)),
    path('api/comment/', include(comment_api_router.urls))
]
