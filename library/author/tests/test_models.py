from django.test import TestCase
from author.models import Author


class AuthorModelTestCase(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(name="Jack", age=32)

    def test_author_str(self):
        self.assertEquals(str(self.author), self.author.name)
