import logging
from celery import shared_task
from books.models import Book
from author.models import Author

@shared_task
def send_daily_statistic():
    number_of_books = Book.objects.count()
    number_of_authors = Author.objects.count()
    message = f"Number of books: {number_of_books}. Number of authors: {number_of_authors}."
    logging.info(message)
    return message