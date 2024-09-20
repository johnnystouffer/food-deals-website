from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.filter(approved=True)
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action == 'create':
            # Only allow admin users to create deals
            return [permissions.IsAdminUser()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Optionally, restrict update and delete actions
            return [permissions.IsAdminUser()]
        else:
            # Allow read-only access to anyone
            return [permissions.AllowAny()]
