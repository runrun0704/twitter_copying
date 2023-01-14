from django.shortcuts import render
import django_filters

from rest_framework import viewsets, filters

from .models import Comment
from .serializer import CommentSerializer

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
