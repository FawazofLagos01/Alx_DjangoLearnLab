# api/urls.py

from django.urls import path, include
from .views import BookList
from rest_framework import DefaultRouter
from .views import BookViewSet

# Create a router instance
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # Include the router URLs
]
