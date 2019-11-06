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
        serializer.save(user=self.request.user)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    lookup_field='OrderName'

