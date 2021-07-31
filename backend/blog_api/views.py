from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.published.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, IsAuthorOrReadOnly):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
