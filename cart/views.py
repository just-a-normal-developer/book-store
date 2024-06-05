from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from books.models import Books
from cart.models import Cart


# class BookBuyingView(LoginRequiredMixin, generic.CreateView):
#
#     model = Cart
#     template_name = "books/book_buying.html"
#     success_url = reverse_lazy("book_buying")
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


class BookBuyingView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Books, id=book_id)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart.added_books.add(book)
        cart.save()

        return redirect('cart_detail')


class CartDetailView(LoginRequiredMixin, TemplateView):
    template_name = "books/cart_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.get(user=self.request.user)
        context['cart'] = cart
        context['total_price'] = cart.total_price
        return context
