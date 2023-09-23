from rest_framework import filters
from books.models import Book


class CommentFilterByBook(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        book_pk = request.query_params.get('book_pk')

        if book_pk:
            try:
                book_id = int(book_pk)
                book = Book.objects.filter(id=book_id).first()
                queryset = queryset.filter(book=book)
            except ValueError:
                pass

        return queryset
