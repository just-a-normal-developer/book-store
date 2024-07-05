# urls.py
from django.urls import path
from .views import payment_verify

urlpatterns = [
    path('payment/verify/', payment_verify, name='payment_verify'),
]
