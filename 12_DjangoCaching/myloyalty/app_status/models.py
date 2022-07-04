from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import uuid


class Bonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Bonus Balance'))

    class Meta:
        verbose_name_plural = _('Bonuses')
        verbose_name = _('Bonus')


class Offer(models.Model):
    offer_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=150, verbose_name=_('Offer Title'))
    subtitle = models.CharField(max_length=600, default=None, blank=True, null=True, verbose_name=_('Offer Subtitle'))
    store = models.ManyToManyField('app_catalog.Store', verbose_name=_('Store Name'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_special_offer = models.BooleanField(verbose_name=_('Is it a special offer?'))
    is_promo_event = models.BooleanField(verbose_name=_('Is it a promo event?'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Offers')
        verbose_name = _('Offer')


# Проверить потом аследуются ли verbose names из родных моделей Foreign Keys
class Purchase(models.Model):
    purchase_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey('app_catalog.Store', on_delete=models.CASCADE)
    category = models.ForeignKey('app_catalog.Category', on_delete=models.CASCADE)
    item = models.ForeignKey('app_catalog.Item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    offer_used = models.ManyToManyField(Offer, blank=True, verbose_name=_('Name of used offer'))
    bonuses_used = models.FloatField(default=0, verbose_name=_('Amount of used bonuses'))

    class Meta:
        verbose_name_plural = _('Purchases')
        verbose_name = _('Purchase')