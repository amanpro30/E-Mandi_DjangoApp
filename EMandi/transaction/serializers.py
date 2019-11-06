from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from transaction.models import Transaction,BankDetails


class BankSerializer(serializers.ModelSerializer):
    #  details=BankdetailSerializer(write_only=True)

    #  def create(self, validated_data):
    #     bankd = validated_data.pop('details')
    #     user= User.objects.get(**validated_data)
    #     BankDetails.objects.create(BankHolder=user, **bankd)
    #     return user

    #  def update(self, instance, validated_data):
    #     detail = validated_data.pop('details')
    #     detail1=instance.username
    #     instance.save()
    #     detail1 = validated_data.get('title', detail1.title)
    #     detail1.BankName = validated_data.get('BankName', detail1.BankName)
    #     detail1.BranchName = validated_data.get('BranchName', detail1.BranchName)
    #     detail1.Ifsc = validated_data.get('Ifsc', detail1.Ifsc)
    #     detail1.AccountNumber = validated_data.get('AccountNumber', detail1.AccountNumber)
    #     detail1.save()
    #     return instance
     class Meta:
        model = User
        fields = ('username',)


class BankdetailSerializer(serializers.ModelSerializer):
      user=serializers.ReadOnlyField(source='user.username')
      class Meta:
        model = BankDetails
        fields = ('id','user','BankName', 'BranchName', 'Ifsc','AccountNumber',)
        read_only_fields=[ 'user']
