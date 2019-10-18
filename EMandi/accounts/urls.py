from django.urls import path, include
from .import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from accounts import views as user_views
from .views import *

app_name = "accounts"


urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='user_login'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/password/',views.change_password,name='change_password'),
    path('change-password/', views.change_password, name='change_password'),
    url(r'^profile/(?P<pk>\d+)/$',views.view_profile,name='view_profile_with_pk'),
    
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('signup/',signup.as_view()),
    
    

]