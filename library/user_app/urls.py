from rest_framework import routers
from django.urls import path, include
from .views import UserDetail

# router = routers.SimpleRouter()
# router.register("user", UserDetail)
urlpatterns = [
    path('user/', UserDetail.as_view())
]