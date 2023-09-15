from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Book
from .serializers import BookSerializer


class BookCreateListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        author_age = self.request.query_params.get('author_age')

        if author_age:
            try:
                author_age = int(author_age)
                queryset = queryset.filter(author__age__gte=author_age)
            except ValueError:
                pass

        return queryset


    def perform_create(self, serializer):
        title = serializer.validated_data.get('title', '') + '!'
        serializer.save(title=title)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer