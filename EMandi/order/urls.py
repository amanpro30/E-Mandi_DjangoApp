from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

app_name = "order"

urlpatterns = [
    
    path('marketorder/', views.OrderList.as_view()),
    path('marketorder/<id>/<price>/', views.OrderDetail.as_view()),
    path('marketorder/<id>/', views.OrderListId.as_view()),
    path('myorder/',views.OrderDetailSelf.as_view()),
    path('myorderexec/',views.OrderDetailSelfExectued.as_view()),
    path('futureexec/',views.FutureDetailSelfExectued.as_view()),
    path('otherorder/',views.OrderDetailOther.as_view()),
    path('myfutures/',views.FutureDetailSelf.as_view()),
    path('otherfutures/',views.FutureDetailOther.as_view()),
    path('getbid/order/<order>/',views.BidListByOrder.as_view()),
    path('getbid/curruser/',views.BidListUser.as_view()),
    path('getbid/<id>/',views.BidListUpdate.as_view()),
    path('getbids/',views.AllBids.as_view()),
    path('futurecontract/<cropName>/<cropVariety>/',views.futurecontract.as_view()),
    path('futurecontract/<id>/', views.OrderDetail_future.as_view()),
    path('futurecontractupdate/<id>/', views.futurecontractupdate.as_view()),
    path('futurecontract/',views.futurecontractlist.as_view()),
    path('futurebid/<order>/',views.FutureBids.as_view()),
    path('cropcity/<city>/',views.Citycropquant.as_view()),
    path('cropcity1/<cropname>/',views.Cropcityquant.as_view()),
    path('cropcity/<cropname>/<city>/',views.Quantcropcity.as_view()),
    path('futurebidupdate/<id>/',views.FutureBidUpdate.as_view()),
    path('crop/<cropName>/<cropVariety>/', views.OrderFilter.as_view()),
    path('executedorder/',views.ExecutedOrderView.as_view()),
    path('futurecontract/<id>',views.FutureDetail.as_view()),
]
