from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status, generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404
from drf_project5_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    '''
    Get all profiles and list them
    '''
    serializer_class = ProfileSerializer

    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
    Get one profile and if you are the owner you can edit
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')