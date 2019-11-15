from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from order.models import ExecutedOrder

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length =100, default='')
    phone = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to='image_profile', blank=True)
    state = models.CharField(max_length =100, default='')
    city = models.CharField(max_length =100, default='')
    street = models.CharField(max_length =500, default='')
    aadharcard = models.BigIntegerField( default=0)
    pincode = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class UserReview(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating=models.FloatField(default=0.0)
    count=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class OrderReview(models.Model):
    order=models.ForeignKey(ExecutedOrder, on_delete=models.CASCADE)
    rating=models.FloatField(default=0.0)
    review=models.CharField(max_length =500, default='')

    def __str__(self):
        return f'{self.order.orderid.CropName}{self.order.buyerid.username} OrderReview'

