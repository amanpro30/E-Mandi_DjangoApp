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
from django.db.models import Q

from django.contrib.auth.models import User

class OrderList(generics.ListCreateAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user,OrderStatus='1')

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    lookup_field='id'

class BidList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    lookup_field='id'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    lookup_field='id'

class OrderDetailSelf(generics.ListCreateAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return MarketOrder.objects.filter(user=user_instance)

class OrderDetailOther(generics.ListCreateAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return MarketOrder.objects.filter(~Q(user=user_instance))
 
