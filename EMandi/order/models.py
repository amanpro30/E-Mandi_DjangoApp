from django.db import models
from django.contrib.auth.models import User
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
    commision=models.FloatField(default=None)


    def __str__(self):
       return f'{self.orderid.CropName}{self.buyerid.username} ExecuteOrder'

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


