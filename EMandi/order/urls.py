from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

app_name = "order"

urlpatterns = [
    
    path('marketorder/', views.OrderList.as_view()),
    path('marketorder/<id>/', views.OrderDetail.as_view()),
    path('myorder/',views.OrderDetailSelf.as_view()),
    path('myorderexec/',views.OrderDetailSelfExectued.as_view()),
    path('otherorderexecu/',views.OrderDetailSelfExectued.as_view()),
    path('getbid/order/<order>/',views.BidListByOrder.as_view()),
    path('getbid/curruser/<order>/',views.BidListUser.as_view()),
    path('getbid/<id>/',views.BidListUpdate.as_view()),
    path('futurecontract/<cropName>/<cropVariety>/',views.futurecontract.as_view()),
    path('futurecontractupdate/<id>/', views.futurecontractupdate.as_view()),
    path('futurecontract/',views.futurecontractlist.as_view()),
    path('futurebid/<order>',views.FutureBids.as_view()),
    path('futurebidupdate/<id>',views.FutureBidUpdate.as_view()),

    path('crop/<cropName>/<cropVariety>/', views.OrderFilter.as_view()),
]
