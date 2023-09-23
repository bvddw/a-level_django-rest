from rest_framework import serializers
from .models import BorrowRequestModel


class BorrowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRequestModel
        fields = ['book', 'borrower', 'request_date']
