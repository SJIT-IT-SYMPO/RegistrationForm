from django.shortcuts import render
from .models import UserProfile
from registration.serializers import UserProfileSerializer
from rest_framework import mixins
from rest_framework import generics

class user_profile_data(	
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

def list(request):
	data = UserProfile.objects.all() 
	return render(request, 'index.html', {'data': data})