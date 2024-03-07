from django.contrib import admin
from .models import BookModel

# Register your models here.

@admin.register(BookModel)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','author','genre','published_date']