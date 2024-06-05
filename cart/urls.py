from django.urls import path

from cart.views import BookBuyingView

urlpatterns = [
    path("<int:pk>/buying/", BookBuyingView.as_view(), name="book_buying"),
]
