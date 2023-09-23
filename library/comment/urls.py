from rest_framework import routers
from django.urls import path, include
from .views import CommentViewSet, approve_comment, reject_comment

router = routers.SimpleRouter()
router.register("comment", CommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('approve_comment/<int:comment_id>/', approve_comment),
    path('reject_comment/<int:comment_id>/', reject_comment),
]