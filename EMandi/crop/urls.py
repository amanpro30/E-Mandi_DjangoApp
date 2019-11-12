from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crop.views import *


app_name = "crop"

urlpatterns = [
    path('crop/<cropName>', CropVariety.as_view()),
]