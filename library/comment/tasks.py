from celery import shared_task
from .models import Comment

@shared_task
def check_comment_by_admin(comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.is_checked_by_admin = True
        comment.save()
    except Comment.DoesNotExist:
        pass