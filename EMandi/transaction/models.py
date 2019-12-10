from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from accounts.models import *

class BankDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    BankName=models.CharField(max_length=50)
    BranchName=models.CharField(max_length=60)
    Ifsc=models.CharField(max_length=50)
    AccountNumber=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.user.username} BankDetails'

class Transaction(models.Model):
    Customer=models.ForeignKey(User,on_delete=models.CASCADE)
    TransDate=models.DateField(auto_now=False,auto_now_add=True)
    Amount=models.PositiveIntegerField(default=None)
    TransType_choices = (
        ('Debited', 'Debited'),
        ('Credited', 'Credited'),
    )
    TransType = models.CharField(max_length=10, choices=TransType_choices,)
    def __str__(self):
        return f'{self.Customer.username} Transaction'

class Balance(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    availablebalance = models.PositiveIntegerField()
    accountbalance = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.user.username} Balance'


def create_balance(sender, **kwargs):
    if kwargs['created']:
        Balance.objects.create(user=kwargs['instance'],availablebalance = 10000,accountbalance = 10000)
        BankDetails.objects.create(user=kwargs['instance'],BankName="",BranchName="",Ifsc="",AccountNumber="")

        

def create_avgrating(sender, **kwargs):
    if kwargs['created']:
        AvgRating.objects.create(user=kwargs['instance'],avgrating="0")

post_save.connect(create_balance, sender=User)     
post_save.connect(create_avgrating, sender=UserProfile)   
