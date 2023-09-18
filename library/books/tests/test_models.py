from django.test import TestCase
from books.models import Book
from author.models import Author


class BookModelTestCase(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(name="Jack", age=32)
        self.book = Book.objects.create(title="Test Book 1", author=self.author)

    def test_author_book(self):
        self.assertEquals(self.book.author, self.author)

    def test_book_str(self):
        self.assertEquals(str(self.book), self.book.title)