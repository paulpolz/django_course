from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок новости')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey('Category', default=None, on_delete=models.CASCADE, verbose_name='Категория')
    text = models.TextField(verbose_name='Содержание')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name='Флаг активности')
    views_count = models.BigIntegerField(default=0, verbose_name='Количество просмотров')


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    logo = models.ImageField(upload_to='images/cates_logo/', blank=True)


    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Comment(models.Model):
    STATUS_CHOCES = (
        ('arc', 'Archive'),
        ('pub', 'Published'),
        ('del', 'Deleted'),
    )

    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    nickname = models.CharField(max_length=25, blank=True, null=True, verbose_name='Ник неавторизованного комментатора')
    news_item = models.ForeignKey('News', default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='arc', choices=STATUS_CHOCES, verbose_name='Статус комментария')
    comment = models.TextField(max_length=280, verbose_name='Текст комментария')

    @admin.display()
    def comment_shorten(self):
        return (str(self.comment[:15] + '...'))
