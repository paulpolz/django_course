from django.db import models
from django.db.models.deletion import CASCADE
from isbn_field import ISBNField

class Author(models.Model):
    """Table for authors information storage"""
    name = models.CharField(max_length=100, verbose_name='Name')
    surname = models.CharField(max_length=100, verbose_name='Surname')
    date_of_birth = models.DateField(verbose_name='Date of Birth')

    def __str__(self):
        return self.name + ' ' + self.surname

class Book(models.Model):
    """Table for authors information storage"""
    title = models.CharField(max_length=100, verbose_name='Title')
    author_id = models.ForeignKey('Author', default=None, on_delete=models.CASCADE, verbose_name='Author')
    isbn = ISBNField(verbose_name='ISBN')
    year_of_publication = models.IntegerField(default = None, verbose_name='Year of Publication')
    count_of_pages = models.IntegerField(verbose_name='Count of pages')