from django.shortcuts import render
from crop.models import *
from rest_framework import generics
from .serializers import * 
# Create your views here.
class PriceDataView(generics.ListCreateAPIView):
    queryset = PriceData.objects.all()
    serializer_class = PriceDataSerializer

    def get_queryset(self):
        crop = self.kwargs['crop']
        variety = self.kwargs['variety']
        crop_instance = Crop.objects.get(cropName=crop,varietyName=variety)
        return PriceData.objects.filter(crop=crop_instance)