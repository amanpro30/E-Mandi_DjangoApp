from django.db import models

# Create your models here.
class Crop(models.Model):
    cropName=models.CharField(max_length=50)
    varietyName=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return f'{self.cropName}{self.varietyName}'

class PriceData(models.Model):
    crop=models.ForeignKey(Crop,on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField()    
    low=models.FloatField(default=None)
    high=models.FloatField(default=None)
    volume=models.IntegerField(default=0)
    closing=models.FloatField(default=None)
    opening=models.FloatField(default=None)

    def __str__(self):
        return f'{self.crop.cropName}{self.low}'