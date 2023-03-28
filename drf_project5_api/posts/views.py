from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Post
from .serializers import PostSerializer
from django.http import Http404


class PostList(generics.ListCreateAPIView):
    '''
    Get all profiles and list them, create post will
    assign the creator to the post
    '''
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(APIView):
    '''
    Get one post by primary key and return
    '''
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
