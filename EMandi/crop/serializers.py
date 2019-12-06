from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from crop.models import *
from rest_framework import serializers

class CropSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crop
        fields = ('cropName','varietyName')
    
class PriceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceData
        fields = ("__all__")



class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = [ 'user', 'crop' ]