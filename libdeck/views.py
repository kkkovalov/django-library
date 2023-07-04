from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import LibrarySpace, Book

# Create your views here.
def index(request):
    latest_library_list = LibrarySpace.objects.order_by("lib_date_opened")
    context = {"latest_library_list": latest_library_list}
    return render(request, "libdeck/index.html", context)
    # return HttpResponse("Welcome to library crossroads!");

def library(request, library_id):
    try:
        cur_library = LibrarySpace.objects.get(pk=library_id)
    except LibrarySpace.DoesNotExist:
        raise Http404("Library does not exist")
    
    latest_book_list = Book.objects.filter(libdeck_id=library_id)
    context = {"latest_book_list": latest_book_list, "cur_library": cur_library}
    return render(request, "libdeck/library.html", context)

def books(request, library_id, book_id):
    try:
        cur_book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    cur_library = LibrarySpace.objects.get(pk=library_id)
    context = {"book": cur_book, "library": cur_library}
    return render(request, "libdeck/book.html", context)
    return HttpResponse("Here is the book %s" % cur_book.book_title)

 