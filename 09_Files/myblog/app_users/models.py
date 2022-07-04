from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user_login = OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин пользователя')
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона')
    city = models.CharField(max_length=50, verbose_name='Город')
    about_me = models.TextField(max_length=600, null=True, blank=True, verbose_name='О себе')
    avatar = models.FileField(upload_to='users/avatars', verbose_name='Фото профиля')