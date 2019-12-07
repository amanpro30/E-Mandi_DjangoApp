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
from .models import *
from django.contrib.auth.models import User


class OrderList(generics.ListCreateAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user,OrderStatus='1')

class OrderListId(generics.ListAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer
    
    def get_queryset(self):
        orderId = self.kwargs['id']
        return MarketOrder.objects.filter(id=orderId)  



class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def perform_update(self, serializer):
        order_id = self.kwargs['id']
        final_price = self.kwargs['price']
        crop_name = MarketOrder.objects.get(pk=order_id).CropName
        print(crop_name)
        crop_variety = MarketOrder.objects.get(pk=order_id).CropVariety 
        MarketOrder.objects.filter(pk=order_id).update(OrderStatus='2')
        order_instance = MarketOrder.objects.get(pk=order_id)
        crop_instance = Crop.objects.get(cropName=crop_name,varietyName=crop_variety)
        order_record_instance = PriceData.objects.create(crop=crop_instance,price=final_price)
        print(order_instance)
        print(final_price)
        buyer_instance= Bid.objects.get(order=order_instance,price=final_price).user
        executed_order_instance = ExecutedOrder.objects.create(orderid=order_instance,buyerid=buyer_instance)
    lookup_field='id'

class BidListByOrder(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    def get_queryset(self):
        order_id = self.kwargs['order']
        order_instance = MarketOrder.objects.get(id=order_id)
        return Bid.objects.filter(order=order_instance)

    def perform_create(self,serializer):
        order_id = self.kwargs['order']
        order_instance = MarketOrder.objects.get(id=order_id)
        serializer.save(user=self.request.user, order=order_instance)


class AllBids(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

class BidListUser(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    def get_queryset(self):
        user=self.request.user
        user_instance = User.objects.get(username=user)
        return Bid.objects.filter(user=user_instance)  

class BidListUpdate(generics.RetrieveUpdateDestroyAPIView):
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
        return MarketOrder.objects.filter(user=user_instance,OrderStatus="1")

class OrderDetailSelfExectued(generics.ListCreateAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return MarketOrder.objects.filter(user=user_instance,OrderStatus="2")

class OrderDetailOther(generics.ListCreateAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return MarketOrder.objects.filter(~Q(user=user_instance),OrderStatus="1")
 

class futurecontract(generics.ListCreateAPIView):
    queryset = FuturesContract.objects.all()
    serializer_class = futurecontractSerializer


    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        Crop_name = self.kwargs['cropName']
        Crop_variety =self.kwargs['cropVariety']
        crop_instance = Crop.objects.get(cropName=Crop_name,varietyName=Crop_variety)
        return FuturesContract.objects.filter(user=user_instance,Crop=crop_instance)
   
    def perform_create(self,serializer):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        Crop_name = self.kwargs['cropName']
        Crop_variety =self.kwargs['cropVariety']
        crop_instance = Crop.objects.get(cropName=Crop_name,varietyName=Crop_variety)
        serializer.save(user=self.request.user, Crop=crop_instance)

class futurecontractlist(generics.ListAPIView):
    queryset = FuturesContract.objects.all()
    serializer_class = futurecontractSerializer



class OrderFilter(generics.ListAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        # Crop_name = self.kwargs['cropName']
        # Crop_variety =self.kwargs['cropVariety']
        # crop_instance = Crop.objects.get(cropName=Crop_name,varietyName=Crop_variety)
        return FuturesContract.objects.filter(user=user_instance,)#,Crop=crop_instance)


# class orderupdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset=MarketOrder.objects.all()
#     serializer_class = MarketSerializer


#     def perform_update(self,serializer):
#         order_id = self.kwargs['order']

#         serializer.save(user=self.request.user,)


class futurecontractupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=FuturesContract.objects.all()
    serializer_class = futurecontractSerializer
    lookup_field ="id"

    def perform_update(self,serializer):
        serializer.save(user=self.request.user,)


class FutureBids(generics.ListCreateAPIView):
    queryset = FutureBid.objects.all()
    serializer_class = FutureBidSerializer
    
    def get_queryset(self):
        order_id = self.kwargs['order']
        order_instance = FuturesContract.objects.get(id=order_id)
        return FutureBid.objects.filter(order=order_instance)

    def perform_create(self,serializer):
        order_id = self.kwargs['order']
        order_instance = FuturesContract.objects.get(id=order_id)
        serializer.save(user=self.request.user, order=order_instance)

class FutureBidUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = FutureBid.objects.all()
    serializer_class = FutureBidSerializer
    lookup_field = 'id'
    def perform_update(self, serializers):
        serializer.save(user=self.request.user)
        cn = self.kwargs['cropName']
        cv = self.kwargs['cropVariety']
        return MarketOrder.objects.filter(~Q(user=user_instance),CropName=cn, CropVariety=cv)

class Citycropquant(generics.ListAPIView):
    queryset = CityCrop.objects.all()
    serializer_class = CitycropSerializer


    def get_queryset(self):

        city = self.kwargs['city']
        return CityCrop.objects.filter(city=city).order_by('-quantity')

class Cropcityquant(generics.ListAPIView):
    queryset = CityCrop.objects.all()
    serializer_class = CitycropSerializer


    def get_queryset(self):

        cropname = self.kwargs['cropname']
        return CityCrop.objects.filter(cropname=cropname).order_by('-quantity')

class Quantcropcity(generics.ListAPIView):
    queryset = CityCrop.objects.all()
    serializer_class = CitycropSerializer


    def get_queryset(self):

        cropname = self.kwargs['cropname']
        city = self.kwargs['city']

        return CityCrop.objects.filter(cropname=cropname,city=city).order_by('-quantity')

class ExecutedOrderView(generics.ListAPIView):
    queryset = ExecutedOrder.objects.all()
    serializer_class = ExecutedOrderSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return ExecutedOrder.objects.filter(buyerid=user_instance)