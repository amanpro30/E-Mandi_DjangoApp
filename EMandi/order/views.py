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


class MarketOrder(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = MarketOrder.objects.all()
    serializer_class = MarketaSerializer
    
    lookup_field='id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save( Created_by=self.request.user)
    
    # def put(self, request, id=None):
    #     return self.update(request, id)
    
    # def perform_update(self, serializer):
    #     serializer.save(Created_by=self.request.user)

    # def delete(self, request, id=None):
    #     return self.destroy(request, id)


    



# class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = MarketaSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        MarketOrder = self.get_object(pk)
        serializer = MarketaSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)