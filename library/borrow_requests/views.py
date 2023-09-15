from rest_framework.viewsets import ModelViewSet

from .models import BorrowRequestModel
from .serializers import BorrowRequestSerializer
from .filters import BorrowRequestFilter


class BorrowRequestViewSet(ModelViewSet):
    queryset = BorrowRequestModel.objects.all()
    serializer_class = BorrowRequestSerializer
    filter_backends = [BorrowRequestFilter]
