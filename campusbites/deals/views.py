from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostView(viewsets.ModelViewSet):
    query = Post.objects.filter(approved=True)
