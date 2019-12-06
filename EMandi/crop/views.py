from django.shortcuts import render
from crop.models import *
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import * 
from crop.serializers import *
# Create your views here.

class PriceDataView(generics.ListCreateAPIView):
    queryset = PriceData.objects.all()
    serializer_class = PriceDataSerializer

    def get_queryset(self):
        crop = self.kwargs['crop']
        variety = self.kwargs['variety']
        crop_instance = Crop.objects.get(cropName=crop,varietyName=variety)
        return PriceData.objects.filter(crop=crop_instance)

class priceDataView(generics.ListAPIView):
    queryset = PriceData.objects.all()
    serializer_class = PriceDataSerializer

class CropTypes(generics.ListAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

    def get_queryset(self):
        return Crop.objects.values('cropName').distinct()

class CropVariety(generics.ListAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

    def get_queryset(self):
        cn = self.kwargs['cropName']
        return Crop.objects.filter(cropName=cn)
       
       
class WatchListView(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class WatchListCreate(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def perform_create(self,serializer):
        crop_name = self.kwargs['crop']
        variety_name = self.kwargs['variety']
        crop_instance = Crop.objects.get(cropName=crop_name,varietyName=variety_name)
        user_instance = User.objects.get(username=self.request.user)
        watchlist_instance = WatchList(user=user_instance, crop=crop_instance)
        watchlist_instance.save()
        # serializer.save(user=user_instance, crop=crop_instance)