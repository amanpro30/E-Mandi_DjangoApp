from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from transaction.models import *


class BankSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ('username',)


class BankdetailSerializer(serializers.ModelSerializer):
      user = serializers.ReadOnlyField(source='user.username')
      class Meta:
        model = BankDetails
        fields = ('id','user','BankName', 'BranchName', 'Ifsc','AccountNumber',)
        read_only_fields=[ 'user']

class BankUpdateSerializer(serializers.ModelSerializer):
        bank = BankdetailSerializer(write_only=True)
        def update(self, instance, validated_data):
                print('instance')
                print(instance.bankdetails)
                bank_data= validated_data.pop('bank')
                bank1=instance.bankdetails
                instance.save()
                bank1.BankName= bank_data.get('BankName', bank1.BankName)
                bank1.BranchName= bank_data.get('BranchName', bank1.BranchName)
                bank1.Ifsc= bank_data.get('Ifsc', bank1.Ifsc)
                bank1.AccountNumber= bank_data.get('AccountNumber', bank1.AccountNumber)
                bank1.save()
                return instance

        class Meta:
                model = User
                fields = ('username','bank')
                

class BalanceSerializer(serializers.ModelSerializer):
        user = serializers.ReadOnlyField(source='user.username')
        class Meta:
                model = Balance
                fields = ('availablebalance','accountbalance', 'user')
                read_only_fields=[ 'user']

class BalanceUpdateSerializer(serializers.ModelSerializer):
    balance=BalanceSerializer(write_only=True)
    
    def update(self, instance, validated_data):
        balance_data= validated_data.pop('balance')
        balance1=instance.balance
        instance.save()
        balance1.availablebalance= balance_data.get('availablebalance', balance1.availablebalance)
        balance1.accountbalance= balance_data.get('accountbalance', balance1.accountbalance)
       # print(balance1)
        balance1.save()
        return instance

    class Meta:
        model = User
        fields = ('username', 'balance', )



