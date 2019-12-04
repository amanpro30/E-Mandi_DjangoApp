from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views
from .views import PriceDataView
from crop.views import *


app_name = "crop"

urlpatterns = [
    path('pricedata/<crop>/<variety>/',PriceDataView.as_view()),
    path('crop/<cropName>/', CropVariety.as_view()),
    path('cropname/', CropTypes.as_view()),
    path('watchlist/<crop>/<variety>/',WatchList.as_view()),
]