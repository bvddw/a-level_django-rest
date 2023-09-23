from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilterByAuthorAge
from comment.models import Comment


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [BookFilterByAuthorAge]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title', '') + '!'
        serializer.save(title=title)

    @action(detail=True, methods=["GET"])
    def commentsBooks(self, request, pk=None):
        book = Book.objects.get(pk=pk)

        comments = Comment.objects.filter(book=book, is_checked_by_admin=True).values_list('id', 'text', 'author')
        return Response({'comments': comments}, status=status.HTTP_200_OK)