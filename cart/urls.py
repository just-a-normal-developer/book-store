from django.urls import path

from cart.views import BookBuyingView, CartDetailView

urlpatterns = [
    path("<int:pk>/buying/", BookBuyingView.as_view(), name="book_buying"),
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
]
