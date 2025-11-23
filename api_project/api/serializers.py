from rest_framework import serializers
from .models import Book  # Make sure your Book model exists in api/models.py

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields of the Book model
