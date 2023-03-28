from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404
from drf_project5_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView()):
    '''
    Get all profiles and list them
    '''
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
    Get one profile and if you are the owner you can edit
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()