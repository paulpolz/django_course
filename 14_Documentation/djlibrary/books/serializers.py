from rest_framework import serializers
from books.models import Author, Book


class AuthorSerializers(serializers.ModelSerializer):
    """ Api Serializer for authors data """
    class Meta:
        model = Author
        fields = ['name', 'surname', 'date_of_birth']


class BookSerializers(serializers.ModelSerializer):
    """ Api Serializer for books data """
    class Meta:
        model = Book
        fields = ['title', 'author_id', 'isbn', 'year_of_publication', 'count_of_pages']