from django.contrib import admin

# Register your models here.
from .models import LibrarySpace, Book

admin.site.register(LibrarySpace)
admin.site.register(Book)