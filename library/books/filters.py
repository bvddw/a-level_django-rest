from rest_framework import filters


class BookFilterByAuthorAge(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        author_age = request.query_params.get('author_age')

        if author_age:
            try:
                author_age = int(author_age)
                queryset = queryset.filter(author__age__gte=author_age)
            except ValueError:
                pass

        return queryset
