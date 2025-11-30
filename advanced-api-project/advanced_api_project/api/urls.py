from django.urls import path
from .views import BookListCreateView, AuthorListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
]