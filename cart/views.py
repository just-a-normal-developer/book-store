from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from books.models import Books
from cart.models import Cart


class BookBuyingView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get("pk")
        book = get_object_or_404(Books, id=book_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart.added_books.add(book)
        cart.save()

        return redirect("cart_detail")


class CartDetailView(LoginRequiredMixin, TemplateView):
    template_name = "cart/cart_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.get(user=self.request.user)
        context["cart"] = cart
        context["total_price"] = cart.total_price
        return context


@login_required
def remove_from_cart(request, book_id):
    cart = get_object_or_404(Cart, user=request.user)
    book = get_object_or_404(Books, id=book_id)
    cart.remove_book(book.id)
    return redirect("cart_detail")
