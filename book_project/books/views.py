from django.views.generic import ListView, DetailView
from .models import Book, Author
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  # Changed from 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'  # Changed from 'books/book_detail.html'
    context_object_name = 'book'

# Author Views
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'  # Changed from 'books/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context