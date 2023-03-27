from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile

class ProfileList(APIView):
    '''
    Profile list view, gets all of the profiles and lists them
    '''
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(profiles)