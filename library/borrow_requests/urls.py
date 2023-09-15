from rest_framework import routers
from django.urls import path, include
from .views import BorrowRequestViewSet

router = routers.SimpleRouter()
router.register("requests", BorrowRequestViewSet)
urlpatterns = [
    path('', include(router.urls))
]