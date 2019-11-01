from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from accounts.models import Transaction,BankDetails


class BankdetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BankDetails
        fields = ( 'BankName', 'BranchName', 'Ifsc','AccountNumber')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    bankdetails= BankdetailSerializer(write_only=True)
    
    # password = serializers.CharField(write_only=True)

    # def get_token(self, obj):
    #     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    #     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    #     payload = jwt_payload_handler(obj)
    #     token = jwt_encode_handler(payload)
    #     return token

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        bank_data = validated_data.pop('bankdetails')
        user_instance = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user_instance, **profile_data)
        password = validated_data.pop('password', None)
        if password is not None:
            user_instance.set_password(password)
        user_instance.save()
        return user_instance
    

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name', 'email','profile')