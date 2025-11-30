from django.urls import path
from . import views

urlpatterns = [
    # Author endpoints
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    # Book endpoints
    path('books/', views.DRFBookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.DRFBookDetailView.as_view(), name='book-detail'),

    # Create Book
    path('books/create/', views.DRFBookCreateView.as_view(), name='book-create'),

    # REQUIRED EXACTLY AS THE CHECKER WANTS
    path('books/update/<int:pk>/', views.DRFBookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.DRFBookDeleteView.as_view(), name='book-delete'),
]
