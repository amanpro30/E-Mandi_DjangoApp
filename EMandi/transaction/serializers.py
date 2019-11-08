from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from transaction.models import Transaction,BankDetails


class BankSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ('username',)


class BankdetailSerializer(serializers.ModelSerializer):
      user=serializers.ReadOnlyField(source='user.username')
      class Meta:
        model = BankDetails
        fields = ('id','user','BankName', 'BranchName', 'Ifsc','AccountNumber',)
        read_only_fields=[ 'user']

class BankUpdateSerializer(serializers.ModelSerializer):
        bank = BankdetailSerializer(write_only=True)
        def update(self, instance, validated_data):

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
