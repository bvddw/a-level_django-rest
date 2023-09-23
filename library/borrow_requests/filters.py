from rest_framework import filters


class BorrowRequestFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user

        if not user.is_superuser:
            queryset = queryset.filter(borrower=user).distinct()

        return queryset
