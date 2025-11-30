from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# ============================
# AUTHOR LIST VIEW (ListView)
# ============================
class AuthorListCreateView(generics.ListCreateAPIView):   # ListView equivalent
    """
    ListView: Returns all authors.
    CreateView: Creates a new author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ============================
# AUTHOR DETAIL VIEW
# ============================
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    DetailView: Retrieve/Update/Delete a specific author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ============================
# BOOK LIST VIEW (ListView)
# ============================
class BookListCreateView(generics.ListCreateAPIView):   # ListView equivalent
    """
    ListView: Returns all books.
    CreateView: Creates a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ============================
# BOOK DETAIL VIEW
# ============================
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    DetailView: Retrieve/Update/Delete a specific book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ============================
# CUSTOM CREATE VIEW
# ============================
class BookCreateView(generics.CreateAPIView):
    """
    CreateView: Create a new book (Authenticated only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ============================
# CUSTOM UPDATE VIEW
# ============================
class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView: Update details of an existing book (Authenticated only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ============================
# CUSTOM DELETE VIEW
# ============================
class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView: Delete a book (Authenticated only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
