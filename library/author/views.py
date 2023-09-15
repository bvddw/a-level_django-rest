from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorSerializer
from books.models import Book


class AuthorCreateListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        book_name = self.request.query_params.get('book_name')

        if book_name:
            queryset = queryset.filter(book__title__icontains=book_name).distinct()

        return queryset

    @action(detail=True, methods=["GET"])
    def authorsBooks(self, request, pk=None):
        author = Author.objects.get(pk=pk)

        books = Book.objects.filter(author=author).values_list('id', flat=True)
        return Response({'books': books}, status=status.HTTP_200_OK)
