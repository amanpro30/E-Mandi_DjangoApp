from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ( 'company', 'state', 'city','street', 'aadharcard', 'pincode', 'phone')
    
    # def create(self, validated_data):
    #     # user_data= validated_data.pop('user')
    #     # username=user_data.pop('username')
    #     # user=User.objects.create(username=username)[0]
    #     profile_data= UserProfile.objects.create(**validated_data)
    #     return profile_data

    # def update(self, instance, validated_data):
    #     # user_data= validated_data.pop('user')
    #     # username=user_data.pop('username')
    #     # user=get_user_model().objects.get_or_create(username=username)[0]
    #     # instance.user=user
    #     instance.company= validated_data.get('company', instance.company)
    #     instance.state= validated_data.get('state', instance.state)
    #     instance.city= validated_data.get('city', instance.city)
    #     instance.street= validated_data.get('street', instance.street)
    #     instance.aadharcard= validated_data.get('aadharcard', instance.aadharcard)
    #     instance.pincode= validated_data.get('pincode', instance.pincode)
    #     instance.phone= validated_data.get('phone', instance.phone)
    #     instance.save()
    #     return instance

class User2Serializer(serializers.ModelSerializer):
    
    profile=ProfileSerializer(write_only=True)
    
    
    class Meta:
        model = User
        fields = ('username', 'profile')

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        # user_instance = User.objects.create(**validated_data)
        # UserProfile.objects.create(user=user_instance, **profile_data)
        # return user_instance    
        raise ValidationError("Wrong method being called")

    def update(self, instance, validated_data):

        profiles_data= validated_data.pop('profile')
        profile1=instance.userprofile
        instance.save()
        profile1.company= profiles_data.get('company', profile1.company)
        profile1.state= profiles_data.get('state', profile1.state)
        profile1.city= profiles_data.get('city', profile1.city)
        profile1.street= profiles_data.get('street', profile1.street)
        profile1.aadharcard= profiles_data.get('aadharcard', profile1.aadharcard)
        profile1.pincode= profiles_data.get('pincode', profile1.pincode)
        profile1.phone= profiles_data.get('phone', profile1.phone)
        profile1.save()
        return instance

class RajaSerializer(serializers.ModelSerializer):
    #user=UserSerializer(write_only=True)
    #user=serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
         model=UserProfile
         fields=('user', 'company',  'city','street', 'aadharcard', 'pincode', 'state',)



class UserSerializerWithToken(serializers.ModelSerializer):

    profile= ProfileSerializer(write_only=True)
    

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token


    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user_instance = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user_instance, **profile_data)
        password = validated_data.pop('password', None)
        if password is not None:
            user_instance.set_password(password)
        user_instance.save()
        return (user_instance)
    

    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name', 'last_name', 'email','profile')

