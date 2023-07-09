from django.db import models

# Create your models here.
class LibrarySpace(models.Model):
    lib_name = models.CharField(max_length=300,blank=False,verbose_name="Library name")
    lib_date_opened = models.DateTimeField(verbose_name="Date opened")
    lib_address = models.CharField(max_length=400, verbose_name="Address")
    lib_book_count = models.IntegerField(verbose_name="Book count", default=0)
    
    def __str__(self):
        return self.lib_name
    
    
class Book(models.Model):
    libdeck_id = models.ForeignKey(LibrarySpace, on_delete=models.CASCADE, related_name="books")
    book_title = models.CharField(max_length=200, verbose_name="Title")
    book_author = models.CharField(max_length=200, verbose_name="Author")
    book_pub_date = models.DateField(verbose_name="Date published", blank=True)
    book_pages = models.IntegerField(default=0, verbose_name="Pages")
    
    def __str__(self):
        return self.book_title

    
