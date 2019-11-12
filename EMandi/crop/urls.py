from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
<<<<<<< HEAD
from order import views
from .views import PriceDataView
=======
from crop.views import *

>>>>>>> d711ae25a31b4c0a411dfd7c1585708635792290

app_name = "crop"

urlpatterns = [
<<<<<<< HEAD
    path('pricedata/<crop>/<variety>/',PriceDataView.as_view()),
=======
    path('crop/<cropName>', CropVariety.as_view()),
>>>>>>> d711ae25a31b4c0a411dfd7c1585708635792290
]