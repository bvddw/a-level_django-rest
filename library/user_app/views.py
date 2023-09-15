from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserSerializer


class UserDetail(APIView):

    def get_object(self):
        return self.request.user

    def get(self, request):
        user = self.get_object()
        serializer = UserSerializer(user)
        ctx = {
            "id": serializer.data['id'],
            "username": serializer.data['username'],
        }
        return Response(ctx)
