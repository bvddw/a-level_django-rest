from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from author.models import Author
from user_app.models import UserModel


class AuthorViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create(username="user", password="newPowerfulPass1")
        self.author = Author.objects.create(name="Jack", age=32)

    def test_lists_authors(self):
        response = self.client.get(reverse("authors-list"))
        self.assertEquals(response.status_code, status.HTTP_200_FORBIDDEN)
        self.assertEquals(len(response.data), 1)

        author = Author.objects.create(name="William", age=30)
        response = self.client.get(reverse("authors-list"))
        self.assertEquals(len(response.data), 2)

    def test_author_detail(self):
        response = self.client.get(reverse("authors-detail", args=[self.author.pk]))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_author_create_forbidden(self):
        url = reverse("authors-list")
        new_data = {
            "name": "Charles",
            "age": "44",
        }
        response = self.client.post(url, new_data)
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_create(self):
        self.client.force_login(self.user)
        url = reverse("authors-list")
        new_data = {
            "name": "Charles",
            "age": "44",
        }
        response = self.client.post(url, new_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)