from rest_framework import filters


class AuthorBooksFilterByName(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        book_name = request.query_params.get('book_name')

        if book_name:
            queryset = queryset.filter(book__title__icontains=book_name).distinct()

        return queryset
