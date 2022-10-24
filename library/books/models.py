from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length = 250)
    author = models.CharField(max_length = 250)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

