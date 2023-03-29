from .models import Like
from rest_framework import generics, permissions
from .serializers import LikeSerializer
from drf_project5_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    '''
    Get one post by primary key and return
    '''
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
