from django.db import models
from books.models import Book
from user_app.models import UserModel


class Comment(models.Model):
    text = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    is_checked_by_admin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text[:18] + "..."}'
