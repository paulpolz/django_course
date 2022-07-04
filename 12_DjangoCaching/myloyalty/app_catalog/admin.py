from django.contrib import admin
from app_catalog.models import Store, Category, Item


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_id', 'name', 'updated_at']
    list_filter = ['updated_at', 'city']
    search_fileds = ['name', 'city', 'updated_at', 'about']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_id', 'store', 'title', 'price']
    list_filter = ['store', 'category', 'updated_at']
    search_fileds = ['title', 'updated_at', 'description']
