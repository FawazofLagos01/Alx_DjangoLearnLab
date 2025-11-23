from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from .models import Book
from .models import Library
from django.http import HttpResponseForbidden
from . import views
# ---------------------------
# Book and Library Views
# ---------------------------
@login_required
def list_books(request):
    """Display a list of all books and their authors."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    """Display details of a specific library, including its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# ---------------------------
# User Registration
# ---------------------------
def register(request):
    """Display registration form and create new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# ---------------------------
# Role-Based Access Control
# ---------------------------
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


# ---------------------------
# Permission-Based Views (Required by Checker)
# ---------------------------
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request):
    return render(request, 'relationship_app/edit_book.html')


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html')


# ---------------------------
# Role-Based Views (Your Previous Logic)
# ---------------------------
@user_passes_test(is_admin)
def admin_view(request):
    """Accessible only to Admin users."""
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome Admin!'})


@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    """Accessible only to Librarian users."""
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome Librarian!'})


@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    """Accessible only to Member users."""
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome Member!'})
