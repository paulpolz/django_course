from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок новости')
    author = models.ForeignKey('Profile', default=None, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey('Category', default=None, on_delete=models.CASCADE, verbose_name='Категория')
    text = models.TextField(verbose_name='Содержание')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(verbose_name='Флаг активности')
    views_count = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_nick = models.CharField(max_length=25, verbose_name='Псевдоним пользователя')
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Фамилия пользователя')
    phone = PhoneNumberField(unique=True, blank=True, null=True, verbose_name='Телефон')
    email = models.EmailField(unique=True, blank=True, null=True, max_length=256, verbose_name='Email')
    is_author = models.BooleanField(verbose_name='Может ли пользователь публиковать новости?')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.user_nick})'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    logo = models.ImageField(upload_to='images/cates_logo/', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    STATUS_CHOCES = (
        ('arc', 'Archive'),
        ('pub', 'Published'),
        ('del', 'Deleted'),
    )

    user = models.ForeignKey('Profile', default=None, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    nickname = models.CharField(max_length=25, blank=True, null=True, verbose_name='Ник неавторизованного комментатора')
    news_item = models.ForeignKey('News', default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='arc', choices=STATUS_CHOCES, verbose_name='Статус комментария')
    comment = models.TextField(max_length=280, verbose_name='Текст комментария')

    @admin.display()
    def comment_shorten(self):
        return (str(self.comment[:15] + '...'))