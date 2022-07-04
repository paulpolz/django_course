from django.urls import path
from books.api import AuthorList, BookList

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors'),
    path('books/', BookList.as_view(), name='books')
]
