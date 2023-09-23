from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .serializers import CommentSerializer
from .filters import CommentFilterByBook
from django.shortcuts import get_object_or_404, redirect
from .tasks import check_comment_by_admin


def approve_comment(request, comment_id):
    if not request.user.is_superuser:
        return redirect('/books/books/')
    comment = get_object_or_404(Comment, id=comment_id)
    comment.is_checked_by_admin = True
    comment.save()

    check_comment_by_admin.delay(comment_id)

    return redirect('/books/books/')


def reject_comment(request, comment_id):
    if not request.user.is_superuser:
        return redirect('/books/books/')
    comment = get_object_or_404(Comment, id=comment_id)
    comment.is_checked_by_admin = False
    comment.save()

    check_comment_by_admin.delay(comment_id)

    return redirect('/books/books/')


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [CommentFilterByBook]
    permission_classes = [IsAuthenticatedOrReadOnly]


