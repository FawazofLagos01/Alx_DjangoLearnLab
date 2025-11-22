from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import register
from .views import admin_view
from .views import librarian_view
from .views import member_view


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
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('register/', views.register, name='register'),

    # ---------------------------
    # Role-Based Access URLs
    # ---------------------------
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
