from django.shortcuts import render
from transaction.models import BankDetails, Balance
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import serializers

class BankList(generics.ListCreateAPIView):
    queryset = BankDetails.objects.all()
    serializer_class = BankdetailSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return BankDetails.objects.filter(user=user_instance)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)



class Update(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = BankUpdateSerializer
    
    lookup_field='username'

class BalanceView(generics.ListAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return Balance.objects.filter(user=user_instance)


class BalanceUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = BalanceUpdateSerializer

    def perform_update(self,serializer):
        serializer.save(user=self.request.user)


    lookup_field="username"

