from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length =100, default='')
    phone = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to='image_profile', blank=True)
    state = models.CharField(max_length =100, default='')
    city = models.CharField(max_length =100, default='')
    street = models.CharField(max_length =500, default='')
    aadharcard = models.BigIntegerField(default=0)
    pincode = models.IntegerField(default=0)





    def __str__(self):
        return self.user.username
