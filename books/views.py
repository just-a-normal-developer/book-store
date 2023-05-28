from django.shortcuts import render , get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
from .models import Books
from .forms import CommentForm


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
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request , 'books/book_detail.html' , {'books' : book ,
                                                        'comments' : book_comments ,
                                                        'Comment_form' : comment_form })

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

