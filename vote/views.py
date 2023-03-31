from rest_framework import generics, permissions
from .models import VoteAlike, VoteNotAlike
from drf_project5_api.permissions import IsOwnerOrReadOnly
from .serializers import VoteAlikeSerializer, VoteNotAlikeSerializer


class VoteAlikeList(generics.ListCreateAPIView):
    '''
    Get all profiles and list them, create post will
    assign the creator to the post
    '''
    serializer_class = VoteAlikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = VoteAlike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteAlikeDetail(generics.RetrieveDestroyAPIView):
    '''
    Get one post by primary key and return
    '''
    serializer_class = VoteAlikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = VoteAlike.objects.all()


class VoteNotAlikeList(generics.ListCreateAPIView):
    '''
    Get all profiles and list them, create post will
    assign the creator to the post
    '''
    serializer_class = VoteNotAlikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = VoteNotAlike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteNotAlikeDetail(generics.RetrieveDestroyAPIView):
    '''
    Get one post by primary key and return
    '''
    serializer_class = VoteNotAlikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = VoteNotAlike.objects.all()