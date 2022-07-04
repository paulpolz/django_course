from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин пользователя')
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='Город')
    is_verified = models.BooleanField(default=False, verbose_name='Может ли пользователь публиковать новости?')
    is_moderator = models.BooleanField(default=False, verbose_name='Является ли пользователь модератором?')
    news_count = models.IntegerField(default=0, verbose_name='Кол-во опубликованных новостей')