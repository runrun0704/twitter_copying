from django.shortcuts import render
import django_filters

from rest_framework import viewsets, filters

from .models import Tag
from .serializer import TagSerializer

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
