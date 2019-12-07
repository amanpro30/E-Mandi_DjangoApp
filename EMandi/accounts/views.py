from django.shortcuts import render,redirect, HttpResponse
from .forms import add_registration_form,RegistrationForm, ChangeProfileForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from order.models import MarketOrder , ExecutedOrder
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from rest_framework import permissions, status, generics, viewsets
from django.contrib.auth.models import User
from rest_framework import permissions, status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAdminUser, AllowAny
from transaction.models import *
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from collections import OrderedDict



def index(request):
    return render(request,'accounts/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        profile_form = add_registration_form(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'image' in request.FILES:
                print('found it')
                profile.image = request.FILES['image']
            profile.save()
            registered = True
            # return redirect("/")
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = RegistrationForm()
        profile_form = add_registration_form()
    return render(request,'accounts/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

@login_required
def view_profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    args={'user':user}
    return render(request,'accounts/profile.html',args)

@login_required
def edit_profile(request):        #edit profile view
    if request.method=='POST':
        form=EditProfileForm(request.POST, instance=request.user)
        form1 = ChangeProfileForm(request.POST, instance=request.user)
        if form.is_valid() and form1.is_valid():
            form.save()
            UserProfile.objects.filter(user=request.user).update(city=request.POST['city'])
            UserProfile.objects.filter(user=request.user).update(phone=request.POST['phone'])
            # UserProfile.objects.filter(user=request.user).update(image=request.POST['image'])

            return redirect('/accounts/profile')
        else:
            return HttpResponse("form  is invalid")

    else:
        form=EditProfileForm(instance=request.user)
        form1=ChangeProfileForm(request.POST,instance=request.user)
        args={'form':form, 'form1':form1}
        return render(request,'accounts/edit_profile.html', args)


@login_required
def change_password(request):        #change password view
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')

    else:
        form=PasswordChangeForm(user=request.user)

        args={'form':form}
        return render(request,'accounts/change_password.html',args)

#====================API PART========================================================================

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    print('&&')
    serializer = UserSerializer(request.user)
    print(request.user)
    user_instance = User.objects.get(username=request.user)
    print(getattr(user_instance,'email'))
    return Response(serializer.data)

class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Signup(generics.ListCreateAPIView):
    serializer_class = UserSerializerWithToken
    permission_classes = (AllowAny,)
    

    def get_queryset(self):
        print('banayenge')
        return User.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializerWithToken(queryset, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        print(request.user)

        k = super().create(request, *args, **kwargs)
        
        current_site = get_current_site(request)
        subject = 'Activate Your MySite Account'
        user_instance= User.objects.get(username=request.data['username'])
        message = render_to_string('accounts/account_activation_email.html', {
            'user': user_instance,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user_instance.pk)),
            'token': account_activation_token.make_token(user_instance),
        })
        user_instance.email_user(subject, message)
        
        return k

def account_activation_sent(request):
    return render(request, 'accounts/account_activation_sent.html')



# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         print(user.__dict__, '*************2222222222', user.userprofile.email_confirmed)
#         user.userprofile.email_confirmed = True
#         user.save()
#         login(request, user)
#         print(user.__dict__, '*************', user.userprofile.email_confirmed)
#         return redirect('http://127.0.0.1:3000')
#     else:
#         return render(request, 'accounts/account_activation_invalid.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        current_user = User.objects.get(pk=uid)
        print(current_user)
    except(TypeError, ValueError, OverflowError):
        current_user = None
    if current_user is not None and account_activation_token.check_token(current_user, token):
        current_user.is_active = True
        current_user.save()
        login(request, current_user)
        return redirect('http://127.0.0.1:3000/login')

    else:
        return render(request,'accounts/account_activation_invalid.html')
        # return HttpResponse('Activation link is invalid')



class profile_change(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = User2Serializer
    queryset = User.objects.all()

    lookup_field = 'username'
    
class profile_change2(generics.ListCreateAPIView):
    queryset=User.objects.all()
    
    serializer_class=User2Serializer
    

    
# class profile_get(generics.ListCreateAPIView):
#     queryset=UserProfile.objects.all()
#     serializer_class=ProfileSerializer
    
    
#     def get_queryset(self):
#         username = self.request.user
#         user_instance = User.objects.get(username=username)
#         return UserProfile.objects.filter(user=user_instance)
        
class profile_get(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        return UserProfile.objects.filter(user=user_instance)
    
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = ProfileSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     print('hello')
    #     return super().create(request, *args, **kwargs)
    # lookup_field='user'
    
    
    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class UsersProfile(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserBasicSerializer

    
    def get_queryset(self):
        username = self.request.user
        user_instance = User.objects.filter(username=username)
        return user_instance

class UsersProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserBasicSerializer

    lookup_field="username"

class userReview(generics.ListCreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserreviewSerializer


    def get_queryset(self):

        username = self.request.user
        user_instance = User.objects.get(username=username)
        user_instance1 = UserProfile.objects.get(user=user_instance)
        return UserReview.objects.filter(revieweduser=user_instance1)
   
    def perform_create(self,serializer):
        username = self.request.user
        user_instance = User.objects.get(username=username)
        user_instance1 = UserProfile.objects.get(user=user_instance)
        rev = self.kwargs['username']
        review_instance = User.objects.get(username=rev)
        review_instance1 = UserProfile.objects.get(user=review_instance)
        # Crop_variety =self.kwargs['cropVariety']
        serializer.save(user=user_instance1, revieweduser=review_instance1,)

class ReviewFilter(generics.ListAPIView):
    queryset = AvgRating.objects.all()
    serializer_class = AvgRatingSerializer

    def get(self, request, city):    
        city_instance = city
        city_instance1=UserProfile.objects.filter(city=city_instance)
        print(city_instance1,'asskjhgfdshgfdshgfdsjhgfd')
        dict1={}
        list1=[]
        for i in city_instance1:
            list=AvgRating.objects.filter(user = i)
            print(list)
            for j in list:
                dict2={}
                dict2 = OrderedDict(
                [('username', j.user.user.username),
                 ('rating', j.avgrating),
                 ('phone', i.phone),
                 ('state', i.state),
                 ('city', i.city),
                 ('pincode', i.pincode),
                 ('email', i.user.email),
                 ])
                list1.append(dict2)
        dict1.update({"users":list1})

        print(dict1)
        # user_instance1 = city_instance1.all()
        return Response(list1)#,Crop=crop_instance)


class peruserReview(generics.ListAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserreviewSerializer


    def get(self,request,username):

        username = self.kwargs['username']
        user_instance = User.objects.get(username=username)
        user_instance1 = UserProfile.objects.get(user=user_instance)
        user_instance2=UserReview.objects.filter(revieweduser=user_instance1)
        dict1={}
        list1=[]
        for i in user_instance2:
            dict2={}
            dict2 = OrderedDict(
            [('user', i.user.user.username),
             ('rating', i.rating),
             ('review', i.review),
             ])
            list1.append(dict2)
        dict1.update({"users":list1})
        return Response(list1)

class getAvgRating(generics.ListAPIView):
    queryset=AvgRating.objects.all()
    serializer_class=AvgRatingSerializer

    def get_queryset(self):
        username= self.kwargs['username']
        user_instance = User.objects.get(username=username)
        user_profile_instance = UserProfile.objects.get(user=user_instance)
        return AvgRating.objects.filter(user=user_profile_instance)

        # return UserReview.objects.filter(revieweduser=user_instance1)

        # def get(self, request, city):    
        # city_instance = city.lower()
        # city_instance1=UserProfile.objects.filter(city=city_instance)
        # print(city_instance1,'asskjhgfdshgfdshgfdsjhgfd')
        # dict1={}
        # list1=[]
        # for i in city_instance1:
        #     list=AvgRating.objects.filter(user = i)
        #     print(list)
        #     for j in list:
        #         dict2={}
        #         dict2 = OrderedDict(
        #         [('username', j.user.user.username),
        #          ('rating', j.avgrating),
        #          ('phone', i.phone),
        #          ('state', i.state),
        #          ('city', i.city),
        #          ('pincode', i.pincode),
        #          ('email', i.user.email),
        #          ])
        #         list1.append(dict2)
        # dict1.update({"users":list1})

        # # print(dict1)
        # # user_instance1 = city_instance1.all()
        # return Response(dict1)#,Crop=crop_instance)