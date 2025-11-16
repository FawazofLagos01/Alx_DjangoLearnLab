from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # ---------------------------
    # Book and Library URLs
    # ---------------------------
    path('books/', login_required(views.list_books), name='list_books'),
    path('library/<int:pk>/', login_required(views.LibraryDetailView.as_view()), name='library_detail'),

    # ---------------------------
    # Authentication URLs
    # ---------------------------
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),

    path('register/', views.register_view, name='register'),

    # ---------------------------
    # Role-Based Access URLs
    # ---------------------------
    path('admin-view/', login_required(views.admin_view), name='admin_view'),
    path('librarian-view/', login_required(views.librarian_view), name='librarian_view'),
    path('member-view/', login_required(views.member_view), name='member_view'),
]
