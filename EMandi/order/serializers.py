from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from order.models import *


class MarketOrderSerializer(serializers.ModelSerializer):
    # market=MarketaSerializer(write_only=True)
    class Meta:
        model = User
        fields = ('username',)


class MarketSerializer(serializers.ModelSerializer):
    Created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MarketOrder
        fields = ('Created_by', 'OrderName','CropName', 'CropVariety', 'Quantity', 'ProductionMode', 'BasePrice', 'OrderStatus',)
        read_only_fields=[ 'Created_by']

class MarketaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarketOrder
        fields = ('id', 'OrderName', 'CropName', 'CropVariety', 'Quantity', 'ProductionMode', 'BasePrice', 'OrderStatus',)

    # def update(self, instance, validated_data):
    #     instance.CropName=validated_data.get('CropName', instance.CropName)
    #     instance.CropVariety = validated_data.get('CropVariety', instance.CropVariety)
    #     instance.Quantity = validated_data.get('Quantity', instance.Quantity)
    #     instance.ProductionMode = validated_data.get('ProductionMode', instance.ProductionMode)
    #     instance.BasePrice = validated_data.get('BasePrice', instance.BasePrice)
    #     instance.OrderStatus = validated_data.get('OrderStatus', instance.OrderStatus)
    #     instance.save()

    #     return instance
