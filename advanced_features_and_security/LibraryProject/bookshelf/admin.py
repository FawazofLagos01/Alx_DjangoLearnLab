from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') #show these columns
    search_fields = ('title', 'author') #add search functionality
    list_filter = ('publication_year',) #add filter by publication year