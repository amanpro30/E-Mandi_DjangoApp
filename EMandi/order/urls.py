from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views

app_name = "order"

urlpatterns = [
    
    path('marketorder/', views.UserList.as_view()),
    path('marketorder/<OrderName>/', views.UserDetail.as_view()),
    #path('update-market-order/<username>', updatemarketorder.as_view()),
    #path('update-market/<int:pk>', UserDetail.as_view()),
    # path('order/', MarketaListView.as_view()),
    # path('order1/<id>/', MarketaListView.as_view()),
    
]
# from rest_framework.urlpatterns import format_suffix_patterns
