from django.db import models

class Order(models.Model):
    random = models.CharField(max_length=200)
    quantity = models.IntegerField()