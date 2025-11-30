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
