from django.urls import path

from cart.views import BookBuyingView, CartDetailView, remove_from_cart

urlpatterns = [
    path("<int:pk>/buying/", BookBuyingView.as_view(), name="book_buying"),
    path('cart/', CartDetailView.as_view(), name='cart_detail'),
    path('remove_from_cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
]
