from django.shortcuts import render
import django_filters

from rest_framework import viewsets, filters

from .models import Good, GoodTweet, GoodComment
from .serializer import GoodSerializer, GoodTweetSerializer, GoodCommentSerializer

# Create your views here.
class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

class GoodTweetViewSet(viewsets.ModelViewSet):
    queryset = GoodTweet.objects.all()
    serializer_class = GoodTweetSerializer

class GoodCommentViewSet(viewsets.ModelViewSet):
    queryset = GoodComment.objects.all()
    serializer_class = GoodCommentSerializer
