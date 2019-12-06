from django.urls import path, include
from .import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from accounts import views as user_views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns



app_name = "accounts"


urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/password/',views.change_password,name='change_password'),
    path('change-password/', views.change_password, name='change_password'),
    url(r'^profile/(?P<pk>\d+)/$',views.view_profile,name='view_profile_with_pk'),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('signup/',Signup.as_view()),
    path('profile1/<username>/', profile_change.as_view()),
    path('profile2/', profile_change2.as_view()),
    path('profile-get/',profile_get.as_view()),
    path('userprofile/',UsersProfile.as_view()),
    path('userreview/<username>/',views.userReview.as_view()),
      path('userreview/',views.peruserReview.as_view()),
    # path('avgrating/<user>/',views.Avgrating.as_view()),
    path('userreview/<city>',views.ReviewFilter.as_view()),
    path('userprofile/<username>/',UsersProfileUpdate.as_view()),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),



]