from django.shortcuts import get_object_or_404
from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.
"""
AuthorListCreateView:
- GET: Returns all authors with their books.
- POST: Creates a new author.
"""

class AuthorListCreateView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
AuthorDetailView:
- GET: Returns a specific author by ID with their books.
"""
class AuthorDetailView(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    
"""
BookListCreateView:
- GET: Returns all books.
- POST: Creates a new book.
"""
class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
BookDetailView:
- GET: Returns a specific book by ID.
"""

class BookDetailView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)