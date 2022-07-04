from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user_login = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User Login'))
    birth_date = models.DateField(verbose_name=_('Date of Birth'))
    phone = PhoneNumberField(unique=True, verbose_name=_('Phone Number'))
    city = models.CharField(max_length=50, verbose_name=_('City'))

    class Meta:
        verbose_name_plural = _('Profiles')
        verbose_name = _('Profile')