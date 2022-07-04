from django.contrib import admin
from books.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'date_of_birth']

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_id', 'year_of_publication', 'count_of_pages']

admin.site.register(Book, BookAdmin)