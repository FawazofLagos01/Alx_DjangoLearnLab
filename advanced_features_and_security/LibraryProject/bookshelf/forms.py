from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """Secure form for creating and editing books."""
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        return title.strip()

    def clean_author(self):
        author = self.cleaned_data.get('author', '')
        return author.strip()

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year and (year < 0 or year > 2100):
            raise forms.ValidationError("Invalid year.")
        return year
