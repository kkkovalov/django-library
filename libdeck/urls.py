from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:library_id>/", views.library, name="Library page"),
    path("<int:library_id>/<int:book_id>/", views.books, name="Book page"),
]
