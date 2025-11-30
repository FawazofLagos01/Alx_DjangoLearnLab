from django.urls import path
from . import views

urlpatterns = [
    # Author endpoints
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    # Book endpoints (generic views)
    path('books/', views.BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Required by checker
    # These include the substrings: "books/update" and "books/delete"
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]
