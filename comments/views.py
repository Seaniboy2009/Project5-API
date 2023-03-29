from rest_framework import generics, permissions
from .models import Comment
from drf_project5_api.permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, CommentDetailSerializer
from django.http import Http404


class CommentList(generics.ListCreateAPIView):
    '''
    Get all comments and list them, create comment will
    assign the creator to the comment
    '''
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Get one post by primary key and return
    '''
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
