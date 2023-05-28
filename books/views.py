from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import Books
from django.urls import reverse_lazy
# Create your views here.

class BookListView(generic.ListView):
    model = Books
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'

# class BookDetailView(generic.DetailView):
#     model = Books
#     template_name = 'books/book_detail.html'
def book_detail_view(request , pk):
    book = get_object_or_404(Books , pk=pk)
    book_comments = book.comments.all()
    return render(request , 'books/book_detail.html' , {'books' : book , 'comments' : book_comments , })

class BookCreateView(generic.CreateView):
    model = Books
    fields = ['title', 'author', 'description', 'price', 'cover',]
    template_name = 'books/book_create.html'

class BookUpdateView(generic.UpdateView):
    model = Books
    fields = ['title' , 'author' , 'description' , 'cover' , ]
    template_name = 'books/book_update.html'

class BookDeleteView(generic.DeleteView):
    model = Books
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

