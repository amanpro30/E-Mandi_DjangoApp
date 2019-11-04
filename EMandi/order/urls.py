from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
# from .models import *

app_name = "order"

urlpatterns = [
    
    path('marketorder/', MarketOrder.as_view()),
    path('marketorder/<id>/', MarketOrder.as_view()),
    #path('update-market-order/<username>', updatemarketorder.as_view()),
    #path('update-market/<int:pk>', UserDetail.as_view()),
    # path('order/', MarketaListView.as_view()),
    # path('order1/<id>/', MarketaListView.as_view()),
    

]