from django.urls import path
from .views import BookCreateListView, BookDetailView

urlpatterns = [
    path('', BookCreateListView.as_view()),
    path('<int:pk>', BookDetailView.as_view())
]