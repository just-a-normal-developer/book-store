from django.shortcuts import render
from django.views import generic
from .models import Books
# Create your views here.

class BookListView(generic.ListView):
    model = Books
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'books/book_detail.html'
