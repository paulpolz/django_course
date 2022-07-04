from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user_login = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Логин пользователя'))
    phone = PhoneNumberField(unique=True, verbose_name=_('Номер телефона'))
    city = models.CharField(max_length=50, verbose_name=_('Город'))
    about_me = models.TextField(max_length=600, null=True, blank=True, verbose_name=_('О себе'))
    avatar = models.FileField(upload_to='users/avatars', verbose_name=_('Фото профиля'))

    class Meta:
        verbose_name_plural = _('профили')
        verbose_name = _('профиль')