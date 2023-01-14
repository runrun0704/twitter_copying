from django.shortcuts import render
import django_filters

from rest_framework import viewsets, filters

from .models import GoodTweet, GoodComment
from .serializer import GoodTweetSerializer, GoodCommentSerializer

# Create your views here.
class GoodTweetViewSet(viewsets.ModelViewSet):
    queryset = GoodTweet.objects.all()
    serializer_class = GoodTweetSerializer

class GoodCommentViewSet(viewsets.ModelViewSet):
    queryset = GoodComment.objects.all()
    serializer_class = GoodCommentSerializer
