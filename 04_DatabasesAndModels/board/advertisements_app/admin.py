from django.contrib import admin
from advertisements_app.models import Advertisements, AdvertisementStatus, AdvertisementType, AdvertisementAuthor, \
    AdvertisementCategory

# Register your models here.


@admin.register(Advertisements, AdvertisementStatus, AdvertisementType, AdvertisementAuthor, AdvertisementCategory)
class AdvertisementAdmin(admin.ModelAdmin):
    pass