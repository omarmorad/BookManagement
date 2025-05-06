from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author
from django import forms
def homepage(request):
    return render(request, 'home.html')

# Book views
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  # Changed from 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'  # Changed from 'books/book_detail.html'
    context_object_name = 'book'

# Author views
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
        context['books'] = Book.objects.filter(author=self.object)
        return context

# New views for book management
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publish_date', 'price', 'appropriate_age', 'image']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-select'}),
            'appropriate_age': forms.Select(attrs={'class': 'form-select'}),
        }

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')