from django.db import models
from django.contrib.auth.models import User

class MarketOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    CropName=models.CharField(max_length=50)
    CropVariety=models.CharField(max_length=50)
    Quantity=models.PositiveIntegerField(default=None)
    OrderDate=models.DateTimeField(auto_now=False,auto_now_add=True)
    ClosingDate=models.DateTimeField(auto_now=False,auto_now_add=False)
    ProductionMode=models.CharField(max_length=50)
    BasePrice=models.FloatField(default=None)
    OrderStatus=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username}{self.CropName}MarketOrder'

class Bid(models.Model):
    orderid=models.ForeignKey(MarketOrder,on_delete=models.CASCADE,null=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    price=models.FloatField(default=None)

    def __str__(self):
        return f'{self.orderid.CropName}{self.userid.username} Bid'

# class Bid(models.Model):
#     #bidid=models.ForeignKey(Bidmid,on_delete=models.CASCADE,null=True)
#     price=models.FloatField(default=None)
#     def __str__(self):
#         return f'{self.price} '
class ExecutedOrder(models.Model):
    orderid=models.OneToOneField(MarketOrder,on_delete=models.CASCADE)
    buyerid=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True,auto_now_add=False)
    commision=models.FloatField(default=None)


    def __str__(self):
       return f'{self.orderid.CropName}{self.buyerid.username} ExecuteOrder'




