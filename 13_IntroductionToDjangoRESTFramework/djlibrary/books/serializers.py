from rest_framework import serializers
from books.models import Author, Book


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'date_of_birth']


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author_id', 'isbn', 'year_of_publication', 'count_of_pages']