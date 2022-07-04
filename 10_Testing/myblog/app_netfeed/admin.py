from django.contrib import admin
from app_netfeed.models import Feeds, Images


class ImageInline(admin.TabularInline):
    model = Images


@admin.register(Feeds)
class FeedsAdmin(admin.ModelAdmin):
    # inlines = [ImageInline]
    pass
