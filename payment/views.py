from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.conf import settings
from cart.models import Cart
import requests


def payment_request(request):
    cart = Cart.objects.get(user=request.user)
    total_price = cart.total_price

    # Replace with actual payment gateway parameters and URL
    payment_gateway_url = "https://paymentgateway.com/initiate_payment"
    merchant_id = "your_merchant_id"
    callback_url = request.build_absolute_uri("/payment/verify/")

    data = {
        "merchant_id": merchant_id,
        "amount": total_price,
        "callback_url": callback_url,
        "description": "Payment for cart items",
    }

    response = requests.post(payment_gateway_url, data=data)
    payment_data = response.json()

    if payment_data["status"] == "success":
        return redirect(payment_data["payment_url"])
    else:
        return render(request, "payment/error.html", {"error": payment_data["error"]})


@csrf_exempt
def payment_verify(request):
    if request.method == "POST":
        payment_status = request.POST.get("status")
        if payment_status == "success":
            return HttpResponse("Payment Successful!")
        else:
            return HttpResponse("Payment Failed.")
    return HttpResponse("Invalid request.")
