from django.urls import path
from .views import NotificationListView, FeedView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
    path('feed/', FeedView.as_view(), name='feed'),
]

