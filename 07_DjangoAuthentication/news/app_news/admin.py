from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db.models.query import QuerySet
from app_news.models import News, Profile, User, Category, Comment


class NewsInline(admin.TabularInline):
    model = News


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Profile)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['user_nick', 'first_name', 'last_name', 'is_author']
    inlines = [NewsInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    # comment = 'comment'
    # if len(comment) > 15:
    #     comment2 = comment[0:14] + '...'
    # else:
    #     comment2 = comment

    list_display = ['user', 'status', 'comment_shorten']
    list_filter = ['user']

    actions = ['deleted_by_admin']

    def deleted_by_admin(self, request, queryset):
        queryset.update(comment='Удалено администратором')

    deleted_by_admin.short_description = 'Удалить комментарий'


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