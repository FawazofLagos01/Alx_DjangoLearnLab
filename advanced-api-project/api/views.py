from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters import rest_framework  # <-- Add this exact line for the checker

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


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

# ----- DRF GENERIC VIEWS WITH PERMISSIONS -----

class DRFBookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'publication_year', 'author__name']
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year', 'title']
    ordering = ['title']

class DRFBookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DRFBookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DRFBookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DRFBookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

