from django.db import models


class Author (models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.PositiveIntegerField()
