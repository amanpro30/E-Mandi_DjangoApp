from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from order.models import *


class MarketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = MarketOrder
        fields = ('id', 'user','CropName', 'CropVariety', 'Quantity', 'ProductionMode', 'BasePrice', 'ClosingDate')
        read_only_fields=[ 'user']


class UserSerializer(serializers.ModelSerializer):
   # market=serializers.PrimaryKeyRelatedField(many=True, queryset=MarketOrder.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', )
