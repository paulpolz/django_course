from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Store(models.Model):
    store_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=150, verbose_name=_('Store Name'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=150, verbose_name=_('City'))
    street = models.CharField(max_length=150, verbose_name=_('Street'))
    building = models.CharField(max_length=150, verbose_name=_('Building'))
    office = models.CharField(max_length=150, default='Undefined', verbose_name=_('Office'))
    about = models.TextField(max_length=1000, default=None, blank=True, null=True, verbose_name=_('Additional Information'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Stores')
        verbose_name = _('Store')


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=150, verbose_name=_('Category Name'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _('Categories')
        verbose_name = _('Category')


class Item(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=150, verbose_name=_('Item Title'))
    store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name=_('Store'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('Category'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0, verbose_name=_('Item Price'))
    description = models.TextField(max_length=1000, default=None, blank=True, null=True, verbose_name=_('Item Description'))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = _('Items')
        verbose_name = _('Item')