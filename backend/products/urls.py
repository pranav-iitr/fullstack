from django.urls import path
from .views import AudiobookListView, AudiobookDetailView, ReviewCreateView

urlpatterns = [
    path('audiobooks/', AudiobookListView.as_view(), name='audiobook-list'),
    path('audiobooks/<int:pk>/', AudiobookDetailView.as_view(), name='audiobook-detail'),
    path('audiobooks/<int:pk>/reviews/', ReviewCreateView.as_view(), name='review-create'),
]
