from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from crop.models import *




class CropSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Crop
        fields = ('cropName','varietyName')
    
    