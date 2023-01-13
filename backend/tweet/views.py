from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import Tweet, User, TweetTag
from .serializer import TweetSerializer, UserSerializer, TweetTagSerializer
# Create your views here.
class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TweetTagViewSet(viewsets.ModelViewSet):
    queryset = TweetTag.objects.all()
    serializer_class = TweetTagSerializer
