from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilterByAuthorAge


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [BookFilterByAuthorAge]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title', '') + '!'
        serializer.save(title=title)