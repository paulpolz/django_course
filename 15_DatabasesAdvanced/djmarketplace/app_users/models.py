from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user_login = OneToOneField(User, on_delete=models.CASCADE, verbose_name=('User Login'))
    birth_date = models.DateField(verbose_name=('Date of Birth'))
    phone = PhoneNumberField(unique=True, verbose_name=('Phone Number'))
    city = models.CharField(max_length=50, verbose_name=('City'))

    class Meta:
        verbose_name_plural = ('Profiles')
        verbose_name = ('Profile')