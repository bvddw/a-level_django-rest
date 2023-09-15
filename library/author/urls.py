from rest_framework import routers
from django.urls import path, include
from .views import AuthorViewSet

router = routers.SimpleRouter()
router.register("authors", AuthorViewSet)
urlpatterns = [
    path('', include(router.urls))
]
