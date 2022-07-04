from books.models import Author, Book
from books.serializers import AuthorSerializers, BookSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.pagination import PageNumberPagination


class SetPagination(PageNumberPagination):
    """
    Object for setting a pagination where page size is can be changed.
    """
    page_size = 2


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Object for viewing a list of authors which may be filtered by authors' names.
    Adding new authors is also available.
    """
    serializer_class = AuthorSerializers
    pagination_class = SetPagination

    def get_queryset(self):
        queryset = Author.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Object for viewing a list of books which may be filtered by:
    author's name and surname, title and count of pages.
    Adding new books is also available.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    pagination_class = SetPagination

    def get_queryset(self):
        queryset = Book.objects.all()
        # Поиск по автору
        author_name = self.request.query_params.get('author_name')
        author_surname = self.request.query_params.get('author_surname')
        page_count_less = self.request.query_params.get('page_count_less')
        page_count_more = self.request.query_params.get('page_count_more')
        page_count_equal = self.request.query_params.get('page_count_equal')
        # Поиск по названию
        title = self.request.query_params.get('title')
        # Фильтрация
        if author_name:
            author = Author.objects.filter(name=author_name)
            queryset = queryset.filter(author_id__in=author)
        if author_surname:
            author = Author.objects.filter(surname=author_surname)
            queryset = queryset.filter(author_id__in=author)
        if title:
            queryset = queryset.filter(title=title)
        if page_count_less:
            queryset = queryset.filter(count_of_pages__lt=page_count_less)
        if page_count_more:
            queryset = queryset.filter(count_of_pages__gt=page_count_more)
        if page_count_equal:
            queryset = queryset.filter(count_of_pages=page_count_equal)
        
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)