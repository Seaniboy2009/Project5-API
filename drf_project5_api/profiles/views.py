from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404

class ProfileList(APIView):
    '''
    Get all profiles and list them
    '''
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    '''
    Get one profile by primary key and return
    '''
    def get_profile(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        profile = self.get_profile(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)