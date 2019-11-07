from django.shortcuts import render
from order.serializers import *
from rest_framework import permissions, status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order.models import MarketOrder

from django.contrib.auth.models import User

class UserList(generics.ListCreateAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,OrderStatus='1')



class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    lookup_field='id'


class OrderDetail(generics.RetrieveAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    # lookup_field = "user"

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return MarketOrder.objects.filter(user=user_instance)
 
    def list(self, request):
        print('uuuuuu')
        queryset = self.get_queryset()
        print('use')
        print(queryset)
        serializer = MarketSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, format=None):
        orders = [{'CropName':order.CropName,'CropVariety':order.CropVariety,'Quantity':order.Quantity,'ProductionMode':order.ProductionMode,'BasePrice':order.BasePrice,} for order in (self.get_queryset())]
        return Response(orders)
    

