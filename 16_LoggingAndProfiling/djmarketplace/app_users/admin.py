from django.contrib import admin
from app_users.models import Profile


@admin.register(Profile)
class BonusAdmin(admin.ModelAdmin):
    list_display = ['user_login', 'phone']