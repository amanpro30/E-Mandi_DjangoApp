from django.conf.urls import url

from .views import create_payment, execute_payment

urlpatterns = [
    url(r'^create-payment/$', create_payment),
    url(r'^execute-payment/$', execute_payment),
]
