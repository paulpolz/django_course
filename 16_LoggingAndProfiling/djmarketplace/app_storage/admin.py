from django.contrib import admin
from pyrsistent import v
from app_storage.models import Store, Article, Good, Cart, OrderStatus, Order


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_name', 'country', 'updated_at']


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['good_name', 'updated_at']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_id', 'price', 'stock', 'updated_at']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'quantity', 'updated_at']


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['status_id', 'status', 'updated_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'status', 'article', 'quantity', 'updated_at']
