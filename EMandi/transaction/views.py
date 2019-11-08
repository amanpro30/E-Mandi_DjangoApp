from django.shortcuts import render
from transaction.models import BankDetails
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


from rest_framework.views import APIView
from .serializers import BankdetailSerializer, BankSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import serializers
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class BankList(generics.ListCreateAPIView):
    queryset = BankDetails.objects.all()
    serializer_class = BankdetailSerializer
    def perform_create(self,serializer):
            serializer.save(user=self.request.user)

class Update(generics.RetrieveUpdateDestroyAPIView):
        queryset = BankDetails.objects.all()
        serializer_class = BankdetailSerializer
        def perform_update(self,serializer):
            serializer.save(user=self.request.user)

        lookup_field='id'
