from django.test import TestCase
from django.utils import timezone
from books.models import Book
from author.models import Author
from borrow_requests.models import BorrowRequestModel
from user_app.models import UserModel


class BorrowRequestModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create(username="user", password="newPowerfulPass1")
        self.author = Author.objects.create(name="Jack", age=32)
        self.book = Book.objects.create(title="Test Book 1", author=self.author)
        self.borrow_request = BorrowRequestModel.objects.create(book=self.book,
                                                                borrower=self.user,
                                                                request_date=timezone.now().date())

    def test_borrow_request_borrower(self):
        self.assertEquals(self.borrow_request.borrower, self.user)

    def test_borrow_request_book(self):
        self.assertEquals(self.borrow_request.book, self.book)