from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

app_name = "order"

urlpatterns = [
    
    path('marketorder/', views.OrderList.as_view()),
    path('marketorder/<id>/', views.OrderDetail.as_view()),
    path('myorder/',views.OrderDetailSelf.as_view()),
    path('otherorder/',views.OrderDetailOther.as_view()),
    path('getbid/order/<order>/',views.BidListByOrder.as_view()),
    path('getbid/curruser/<order>/',views.BidListUser.as_view()),
    path('getbid/<id>/',views.BidListUpdate.as_view()),
]
