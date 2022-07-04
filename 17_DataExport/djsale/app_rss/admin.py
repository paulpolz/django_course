from django.contrib import admin
from app_rss.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'updated_at']

