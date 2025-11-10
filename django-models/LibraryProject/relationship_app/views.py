from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

def list_books(request):
    """Display a list of all books and their authors."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """Display details of a specific library, including its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Create your views here.
