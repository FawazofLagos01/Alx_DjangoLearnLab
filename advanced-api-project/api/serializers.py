from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

"""
BookSerializer:
- Serializes Book model instances.
- Includes custom validation to prevent future publication years.
"""

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
"""
AuthorSerializer:
- Serializes Author model instances.
- Used a nested BookSerializer to show all books belonging to an author.
- Uses read_only=True to avoid requiring nested book data on author creation.
"""

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']