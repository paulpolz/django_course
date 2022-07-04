from django.contrib import admin
from app_loyalty.models import BalanceStatus, Balance


@admin.register(BalanceStatus)
class BalanceStatusAdmin(admin.ModelAdmin):
    list_display = ['status_id', 'status', 'updated_at']


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'balance', 'updated_at']
