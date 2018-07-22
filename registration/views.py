from django.shortcuts import render
from .models import UserProfile
from registration.serializers import UserProfileSerializer
from rest_framework import mixins
from rest_framework import generics
import csv
from django.http import HttpResponse

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

def download_csv(request):
    f = open('some.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "College", "Phone No"])
    queryset = UserProfile.objects.all()
    for s in queryset:
        writer.writerow([s.name, s.email, s.college, s.phone_no])
    f.close()
    f = open('some.csv', 'r')
    response = HttpResponse(f, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
    return response