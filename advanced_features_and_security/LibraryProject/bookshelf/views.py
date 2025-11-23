from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from .models import Book

# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Your create logic here
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Your edit logic here
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    # Redirect after deletion
    pass

def search_books(request):
    # Validate input to prevent SQL injection
    query = request.GET.get("q", "")
    safe_query = query.strip()

    # Use Django ORM (ORM is SQL-injection safe)
    books = Book.objects.filter(title__icontains=safe_query)

    return render(request, "bookshelf/book_list.html", {"books": books, "query": safe_query})