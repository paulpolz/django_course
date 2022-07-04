from django.contrib import admin
from app_news.models import News, Comments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass
