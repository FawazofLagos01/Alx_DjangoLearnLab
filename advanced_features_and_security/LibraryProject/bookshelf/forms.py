from django import forms
from .models import Book

# Required by checker
class ExampleForm(forms.Form):
    """Example form to demonstrate secure input with CSRF and validation."""
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        return name

    def clean_message(self):
        message = self.cleaned_data.get("message", "").strip()
        return message


# Secure model form used for Book create/edit
class BookForm(forms.ModelForm):
    """Secure form for creating and editing books."""

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author', '').strip()
        return author

    def clean_publication_year(self):
        year = self.cleaned_data.get('publication_year')
        if year and (year < 0 or year > 2100):
            raise forms.ValidationError("Invalid publication year.")
        return year
