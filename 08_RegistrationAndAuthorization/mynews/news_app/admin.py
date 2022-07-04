from django.contrib import admin
from news_app.models import Category, Comment, News


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'is_active']
    list_filter = ['is_active']
    inlines = [CommentInline]

    actions = ['is_active', 'no_active']

    def is_active(self, request, queryset):
        queryset.update(is_active=True)

    def no_active(self, request, queryset):
        queryset.update(is_active=False)

    is_active.short_description = 'Активно'
    no_active.short_description = 'Неактивно'


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'comment_shorten']
    list_filter = ['user']

    actions = ['deleted_by_admin']

    def deleted_by_admin(self, request, queryset):
        queryset.update(comment='Удалено администратором')

    deleted_by_admin.short_description = 'Удалить комментарий'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']