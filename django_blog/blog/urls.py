from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Blog Post Views
    path('', views.PostListView.as_view(), name='home'),  # Home page showing posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment Views
    path('post/<int:post_pk>/comments/new/', views.add_comment, name='add-comment'),
    path('comments/<int:comment_pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comments/<int:comment_pk>/delete/', views.delete_comment, name='delete-comment'),
]
