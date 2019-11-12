from django.shortcuts import render
from crop.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from crop.models import *

class CropVariety(generics.ListAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

    def get_queryset(self):
        cn = self.kwargs['cropName']
        return Crop.objects.filter(cropName=cn)
       
    