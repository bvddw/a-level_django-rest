from rest_framework.test import APITestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.status import status
from books.models import Book
from author.models import Author
from borrow_requests.models import BorrowRequestModel
from user_app.models import UserModel


class BorrowRequestViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(name="Jack", age=32)
        self.book = Book.objects.create(title="Test Book 1", author=self.author)
        self.user = UserModel.objects.create(username="user", password="newPowerfulPass1")
        self.borrow_request = BorrowRequestModel.objects.create(book=self.book,
                                                                borrower=self.user,
                                                                request_date=timezone.now().date())

    def test_lists_borrow_requests(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("borrow_requests-list"))
        self.assertEquals(response.status_code, status.HTTP_200_FORBIDDEN)
        self.assertEquals(len(response.data), 1)

        author = Author.objects.create(name="William", age=30)
        self.book = Book.objects.create(title="Test Book 2", author=author)
        borrow_request = BorrowRequestModel.objects.create(book=self.book,
                                                           borrower=self.user,
                                                           request_date=timezone.now().date())

        response = self.client.get(reverse("borrow_requests-list"))
        self.assertEquals(len(response.data), 2)

    def test_borrow_request_detail_forbidden(self):
        response = self.client.get(reverse("borrow_requests-detail", args=[self.borrow_request.pk]))
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_borrow_request_detail(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("borrow_requests-detail", args=[self.borrow_request.pk]))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_borrow_request_create_forbidden(self):
        url = reverse("borrow_requests-list")
        new_data = {
            "book": f"{self.book.pk}",
            "borrower": f"{self.user.pk}",
            "request_date": f"{timezone.now().date()}"
        }
        response = self.client.post(url, new_data)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_borrow_request_create(self):
        self.client.force_login(self.user)
        url = reverse("borrow_requests-list")
        new_data = {
            "book": f"{self.book.pk}",
            "borrower": f"{self.user.pk}",
            "request_date": f"{timezone.now().date()}"
        }
        response = self.client.post(url, new_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
