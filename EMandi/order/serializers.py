from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import *

class MarketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = MarketOrder
        fields = ('id', 'user','CropName', 'CropVariety', 'Quantity', 'ProductionMode', 'BasePrice', 'ClosingDate')
        read_only_fields=[ 'user']


class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ('id', 'username','first_name', 'last_name', 'email' )

class BidSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ('id','order', 'price','user')


class BidUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bid
        fields = ('id', 'price',)


class futurecontractSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    Crop = serializers.ReadOnlyField(source='Crop.cropName')

    class Meta:
        model = FuturesContract
        fields = ('id', 'user', 'Crop', 'Quantity', 'OrderDate', 'DeliveryDate', 'ProductionMode', 'AdvanceDate', 'ContractPrice', 'advance', )


class FutureBidSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FutureBid

        fields = ('id' , 'price', 'advance')

class CitycropSerializer(serializers.ModelSerializer):

    class Meta:
        model = CityCrop
        fields = ('id', 'cropname', 'city','quantity')


class ExecutedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutedOrder
        fields = ('orderid','buyerid','date')
