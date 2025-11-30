from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author

# ----- API VIEWS -----

class AuthorListCreateView(ListView):
    model = Author
    template_name = "authors/author_list.html"

class AuthorDetailView(DetailView):
    model = Author
    template_name = "authors/author_detail.html"

# ----- GENERIC BOOK CRUD -----

class BookListCreateView(ListView):
    model = Book
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"

class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = "books/book_form.html"
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = "__all__"
    template_name = "books/book_form.html"
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy('book-list')
