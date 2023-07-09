from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from datetime import datetime

from .models import LibrarySpace, Book

# Create your views here.
def index(request):
    latest_library_list = LibrarySpace.objects.order_by("lib_date_opened")
    context = {"latest_library_list": latest_library_list}
    return render(request, "libdeck/index.html", context)
    # return HttpResponse("Welcome to library crossroads!");


# class IndexView(generic.ListView):
#     template_name = "libdeck/index.html"
#     context_object_name = "latest_library_list"
    
#     def get_queryset(self):
#         return LibrarySpace.objects.order_by("lib_date_opened")


# class LibraryView(generic.ListView):
#     model = LibrarySpace
#     context_object_name = "latest_book_list"    
#     template_name = "libdeck/library.html"
# class BookView(generic.DeleteView):
#     model = Book
#     template_name="libdeck/book.html"


def library(request, library_id):
    
    # SHORTCUT for try & except 404 ERROR
    cur_library = get_object_or_404(LibrarySpace, pk=library_id)
    
    # LONG WAY OF DOING 404 ERROR THROW
    # try:
    #     cur_library = LibrarySpace.objects.get(pk=library_id)
    # except LibrarySpace.DoesNotExist:
    #     raise Http404("Library does not exist")
    
    latest_book_list = Book.objects.filter(libdeck_id=library_id)
    context = {"latest_book_list": latest_book_list, "cur_library": cur_library}
    return render(request, "libdeck/library.html", context)

def books(request, library_id, book_id):
    if request.method == "GET":
        try:
            cur_book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        cur_library = LibrarySpace.objects.get(pk=library_id)
        context = {"book": cur_book, "library": cur_library}
        return render(request, "libdeck/book.html", context)
    elif "delete" in request.POST:
        Book.objects.filter(pk=book_id).delete()
        return HttpResponseRedirect(reverse("libdeck:library_page", args=(library_id,)))
    elif "update" in request.POST:
        return HttpResponseRedirect(reverse("libdeck:book_update", args=(library_id, book_id,)))
    else:
        raise Http404("The page you are trying to access does not exist.")

def newBook(request, library_id):
    cur_library = get_object_or_404(LibrarySpace, pk=library_id)
    if request.method == "GET":
        context = {"library": cur_library}
        return render(request, "libdeck/newbook.html", context)
    elif request.method == "POST":
        try:
            new_book = Book(libdeck_id=cur_library, book_title=request.POST["book_title"], book_author=request.POST["book_author"], book_pub_date=request.POST["book_pub_date"], book_pages=request.POST["book_pages"])
        except(KeyError, Book.DoesNotExist):
            return render(request, "libdeck/newbook.html", context)
        else:
            new_book.save()
            return HttpResponseRedirect(reverse("libdeck:book_page", args=(library_id,new_book.id,)))
    else:
        raise Http404("The page you are trying to access does not exist.")
        
def updateBook(request, library_id, book_id):
    cur_library = get_object_or_404(LibrarySpace, pk=library_id)
    cur_book = get_object_or_404(Book, pk=book_id)
    if request.method == "GET":
        context = {"library": cur_library, "book": cur_book}
        return render(request, "libdeck/updateBook.html", context)
    elif request.method == "POST":
        cur_book.book_title = request.POST.get("book_title", '')
        cur_book.book_author = request.POST.get("book_author", '')
        cur_book.book_pub_date = request.POST.get("book_pub_date")
        cur_book.book_pages = request.POST.get("book_pages", 0)
        cur_book.save()
        return HttpResponseRedirect(reverse("libdeck:book_page", args=(library_id, book_id,)))
    else:
        raise Http404("The page you are trying to access does not exist.")

# def deleteConfirmation(request, library_id, book_id):
#     cur_library = get_object_or_404(LibrarySpace, pk=library_id)
#     cur_book = get_object_or_404(Book, pk=book_id)
#     context = {"library": cur_library, "book": cur_book}
#     return render(request, "libdeck/deleteConfirmation.html", context)
    