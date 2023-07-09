from django.urls import path

from . import views


app_name = "libdeck"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:library_id>/", views.library, name="library_page"),
    path("<int:library_id>/<int:book_id>/", views.books, name="book_page"),
    path("<int:library_id>/newbook/", views.newBook, name="new_book"),
    path("<int:library_id>/<int:book_id>/update/", views.updateBook, name="book_update"),
    # path("<int:library_id>/<int:book_id>/deleteconfirmation/", views.deleteConfirmation, name="delete_confirmation"),
]
