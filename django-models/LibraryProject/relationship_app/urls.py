from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    # ---------------------------
    # Book and Library URLs
    # ---------------------------
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ---------------------------
    # Book CRUD (with permissions)
    # ---------------------------
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # ---------------------------
    # Authentication URLs
    # ---------------------------
    path('login/', auth_views.LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='relationship_app/logout.html'
    ), name='logout'),

    path('register/', views.register_view, name='register'),

    # ---------------------------
    # Role-Based Access URLs
    # ---------------------------
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
