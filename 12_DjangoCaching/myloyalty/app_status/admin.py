from django.contrib import admin
from app_status.models import Bonus, Offer, Purchase


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    search_fields = ['user']


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['offer_id', 'title', 'is_special_offer', 'is_promo_event']
    list_filter = ['store', 'updated_at', 'is_special_offer', 'is_promo_event']
    search_fields = ['title', 'subtitle', 'store', 'updated_at']


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['purchase_id', 'user', 'item', 'updated_at', 'bonuses_used']
    list_filter = ['store', 'category', 'updated_at']
    search_fields = ['purchase_id', 'user', 'item', 'store', 'category', 'updated_at']