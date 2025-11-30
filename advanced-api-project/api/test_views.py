from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()

        # Create Authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create Books
        self.book1 = Book.objects.create(title="Python Basics", publication_year=2022, author=self.author1)
        self.book2 = Book.objects.create(title="Advanced Django", publication_year=2023, author=self.author2)

    # ------------------- TEST LIST VIEW -------------------
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ------------------- TEST CREATE BOOK -------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2025,
            "author": self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {"title": "Fail Book", "publication_year": 2025, "author": self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------- TEST RETRIEVE DETAIL -------------------
    def test_retrieve_book_detail(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # ------------------- TEST UPDATE BOOK -------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-update', args=[self.book1.id])
        data = {"title": "Updated Book", "publication_year": 2024, "author": self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {"title": "Fail Update", "publication_year": 2024, "author": self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------- TEST DELETE BOOK -------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------- TEST FILTERING -------------------
    def test_filter_books_by_author(self):
        url = reverse('book-list') + f'?author__name={self.author1.name}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author1.id)

    # ------------------- TEST SEARCH -------------------
    def test_search_books(self):
        url = reverse('book-list') + '?search=Python'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Python Basics")

    # ------------------- TEST ORDERING -------------------
    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.data[0]['publication_year'], 2023)
