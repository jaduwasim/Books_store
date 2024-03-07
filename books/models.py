from django.db import models

# Create your models here.

class BookModel(models.Model):
    author = models.CharField(max_length=60)
    genre = models.CharField(max_length=50)
    published_date = models.DateField()

    class Meta:
        db_table = 'books_table'