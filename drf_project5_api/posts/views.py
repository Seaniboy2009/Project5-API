from rest_framework import generics, permissions
from .models import Post
from drf_project5_api.permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from django.db.models import Count
from rest_framework import status, generics, filters


class PostList(generics.ListCreateAPIView):
    '''
    Get all profiles and list them, create post will
    assign the creator to the post
    '''
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        alikes_count=Count('alike', distinct=True),
        not_alikes_count=Count('notalike', distinct=True),
    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateAPIView):
    '''
    Get one post by primary key and return
    '''
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
