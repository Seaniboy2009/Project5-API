from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404
from drf_project5_api.permissions import IsOwnerOrReadOnly

class ProfileList(APIView):
    '''
    Get all profiles and list them
    '''
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={ 'request': request })
        return Response(serializer.data)


class ProfileDetail(APIView):
    '''
    Get one profile by primary key and return
    '''
    
    # change the serializer class to be a form for input
    serializer_class = ProfileSerializer
    # Change the permissions class to use custom
    permission_classes = [IsOwnerOrReadOnly]

    def get_profile(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(profile, context={ 'request': request })
        return Response(serializer.data)
    
    def put(self, request, pk):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(profile, data=request.data, context={ 'request': request })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)