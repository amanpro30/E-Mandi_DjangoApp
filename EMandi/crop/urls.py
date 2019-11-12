from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from order import views
from .views import PriceDataView

app_name = "crop"

urlpatterns = [
    path('pricedata/<crop>/<variety>/',PriceDataView.as_view()),
]