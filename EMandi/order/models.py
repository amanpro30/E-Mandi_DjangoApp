from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from accounts.models import UserProfile

from crop.models import *

class MarketOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    CropName=models.CharField(max_length=50)
    CropVariety=models.CharField(max_length=50)
    Quantity=models.PositiveIntegerField(default=None)
    OrderDate=models.DateTimeField(auto_now_add=True)
    ClosingDate=models.DateField(auto_now=False)
    ProductionMode=models.CharField(max_length=50)
    BasePrice=models.FloatField(default=None)
    OrderStatus_choices =(
        ('1', '1'),
        ('2','2'),
        ('3','3'),
    )
    OrderStatus=models.CharField(max_length=10, choices=OrderStatus_choices)

    def __str__(self):
        return f'{self.user.username}{self.CropName}MarketOrder'

class Bid(models.Model):
    order=models.ForeignKey(MarketOrder,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    price=models.FloatField(default=None)

    # def __str__(self):
    #     return f'{self.order.CropName}{self.user.username} Bid'


class ExecutedOrder(models.Model):
    orderid=models.OneToOneField(MarketOrder,on_delete=models.CASCADE)
    buyerid=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True,auto_now_add=False)


    def __str__(self):
       return f'{self.orderid.CropName}{self.buyerid.username} ExecuteOrder'

class CropProduction(models.Model):
    cropname=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    quantity=models.FloatField(default=0.0)
    def __str__(self):
        return str(self.city)

def updatecropproduction(sender, **kwargs):
    if kwargs['created']:
        print(kwargs['instance'].__dict__)
        print(kwargs['instance'].user)
        user_ins=kwargs['instance'].user
        print(user_ins)
        user_instance = UserProfile.objects.get(user=user_ins)
        # user_instance=UserProfile.objects.get(user=user_instance1.id)
        print(user_instance.city)
        city=user_instance.city
        crop_ins=kwargs['instance'].CropName
        # order_instance=MarketOrder.objects.get(id=order_ins.id)
        # quantity_instance=MarketOrder.objects.get(Quantity=order_ins)
        try:
            quantity = CropProduction.objects.get(city=city,cropname=crop_ins).quantity
                        
        except:
            quantity = 0

        new_quantity = quantity + kwargs['instance'].Quantity
        CropProduction.objects.filter(city=city,cropname=crop_ins).delete()
        CropProduction.objects.create(city=city,cropname=crop_ins,quantity=new_quantity)

class CityCrop(models.Model):
    cropname=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    quantity=models.FloatField(default=0.0)
    def __str__(self):
        return str(self.city)

def updatecitycrop(sender, **kwargs):
    if kwargs['created']:
        buyer_instance=kwargs['instance'].buyerid
        city = UserProfile.objects.get(user=buyer_instance).city
        crop_name=kwargs['instance'].orderid.CropName
        Quantity=kwargs['instance'].orderid.Quantity
        try:
            quantity = CityCrop.objects.get(city=city,cropname=crop_name).quantity
        except:
            quantity = 0
        new_quantity = quantity + Quantity
        CityCrop.objects.filter(city=city,cropname=crop_name).delete()
        CityCrop.objects.create(city=city,cropname=crop_name,quantity=new_quantity)

class FuturesContract(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Crop=models.ForeignKey(Crop,on_delete=models.CASCADE)
    # CropVariety=models.CharField(max_length=50)
    Quantity=models.PositiveIntegerField(default=None)
    OrderDate=models.DateField(auto_now_add=True)
    DeliveryDate=models.DateField(auto_now=False)
    AdvanceDate=models.DateField(null=True)
    ProductionMode=models.CharField(max_length=50)
    ContractPrice=models.FloatField(default=None)
    advance=models.FloatField(default=None)
    order_status=models.BooleanField(default=False)

    def __str__(self):
       return f'{self.Quantity}{self.user.username} FutureContract'


class FutureBid(models.Model):
    order=models.ForeignKey(FuturesContract,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    price=models.FloatField(default=None)
    advance=models.FloatField(default=None)

class FutureDeal(models.Model):
    orderid=models.OneToOneField(FuturesContract,on_delete=models.CASCADE)
    buyerid=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True,auto_now_add=False)


post_save.connect(updatecitycrop, sender=ExecutedOrder)
post_save.connect(updatecropproduction, sender=MarketOrder)
