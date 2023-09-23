from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_daily_statistic
from .serializers import UserSerializer


class UserDetail(APIView):

    def get_object(self):
        return self.request.user

    def get(self, request):
        user = self.get_object()
        serializer = UserSerializer(user)
        message = send_daily_statistic.delay()
        result = message.get()
        ctx = {
            "id": serializer.data['id'],
            "username": serializer.data['username'],
            "statistics": result,
        }
        return Response(ctx)
