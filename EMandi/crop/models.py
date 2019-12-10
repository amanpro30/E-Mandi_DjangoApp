from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crop(models.Model):
    cropName=models.CharField(max_length=50)
    varietyName=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return f'{self.cropName}'

class PriceData(models.Model):
    crop=models.ForeignKey(Crop,on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now=True)    
    price = models.FloatField(default=0.0)


class WatchList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE,null=True)