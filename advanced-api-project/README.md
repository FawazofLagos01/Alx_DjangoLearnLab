# advanced-api-project

## Setup
1. python -m venv venv
2. source venv/Scripts/activate
3. pip install -r requirements.txt  # or pip install django djangorestframework
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

## Endpoints
- GET /api/books/          -> list books
- GET /api/books/<pk>/     -> book details
- POST /api/books/create/  -> create (auth required)
- PATCH /api/books/<pk>/update/ -> update (auth required)
- DELETE /api/books/<pk>/delete/ -> delete (auth required)
- GET /api/authors/        -> list authors with nested books



# Advanced API Project

## Django REST Framework API - Testing Documentation

This document outlines the testing approach for the Book and Author API endpoints.

---

## 1. Overview

The purpose of these tests is to ensure the API endpoints for the `Book` and `Author` models work correctly, including:

- CRUD operations
- Filtering, searching, and ordering
- Permissions and authentication

Tests use Django's built-in test framework (`unittest`) and DRF's `APIClient`.

---

## 2. Test Setup

- **Test Database:** Django automatically creates a temporary database during testing.
- **Test Client:** `rest_framework.test.APIClient` is used to simulate HTTP requests.
- **Sample Data:** Minimal `Book` and `Author` instances are created in the `setUp()` method for testing.

---

## 3. Tested Endpoints

### Authors
- `GET /api/authors/` → Retrieve all authors
- `GET /api/authors/<id>/` → Retrieve a specific author

### Books
- `GET /api/books/` → Retrieve all books
- `POST /api/books/` → Create a new book
- `GET /api/books/<id>/` → Retrieve a specific book
- `PUT /api/books/<id>/update/` → Update a book
- `DELETE /api/books/<id>/delete/` → Delete a book

---

## 4. Test Scenarios

### CRUD Operations
- **Create Book:** Verify a book is created successfully and returned with correct data.
- **Retrieve Book:** Verify the details of a specific book by ID.
- **Update Book:** Verify the book data is updated correctly.
- **Delete Book:** Verify the book is removed from the database.

### Filtering, Searching, Ordering
- **Filtering:** Use query parameters like `?author=<id>` or `?publication_year=<year>` to filter results.
- **Searching:** Use `?search=<keyword>` to search book titles or authors.
- **Ordering:** Use `?ordering=title` or `?ordering=-publication_year` to sort results.

### Permissions
- **Authenticated Access:** Verify create, update, and delete endpoints require authentication.
- **Read-Only Access:** Verify list and detail endpoints can be accessed without authentication.

---

## 5. Running Tests

From the project root (where `manage.py` is located):

```bash
python manage.py test api
