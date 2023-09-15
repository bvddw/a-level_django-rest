from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorSerializer
from .filters import AuthorBooksFilterByName
from books.models import Book


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [AuthorBooksFilterByName]

    @action(detail=True, methods=["GET"])
    def authorsBooks(self, request, pk=None):
        author = Author.objects.get(pk=pk)

        books = Book.objects.filter(author=author).values_list('id', flat=True)
        return Response({'books': books}, status=status.HTTP_200_OK)
