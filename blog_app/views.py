from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsAuthorOrReadOnly


# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
