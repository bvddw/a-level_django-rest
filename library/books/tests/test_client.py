from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.status import status
from books.models import Book
from author.models import Author
from user_app.models import UserModel


class BookViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create(username="user", password="newPowerfulPass1")
        self.author = Author.objects.create(name="Jack", age=32)
        self.book = Book.objects.create(title="Test Book 1", author=self.author)

    def test_lists_books(self):
        response = self.client.get(reverse("books-list"))
        self.assertEquals(response.status_code, status.HTTP_200_FORBIDDEN)
        self.assertEquals(len(response.data), 1)

        author = Author.objects.create(name="William", age=30)
        self.book = Book.objects.create(title="Test Book 2", author=author)
        response = self.client.get(reverse("books-list"))
        self.assertEquals(len(response.data), 2)

    def test_book_detail(self):
        response = self.client.get(reverse("books-detail", args=[self.book.pk]))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_book_create_forbidden(self):
        url = reverse("books-list")
        new_data = {
            "title": "Very New Book",
            "author": f"{self.author.pk}",
        }
        response = self.client.post(url, new_data)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_book_create(self):
        self.client.force_login(self.user)
        url = reverse("books-list")
        new_data = {
            "title": "Very New Book",
            "author": f"{self.author.pk}",
        }
        response = self.client.post(url, new_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)