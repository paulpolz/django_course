from users_app.models import Profile
from django.contrib import admin
from users_app.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_verified']


admin.site.register(Profile, ProfileAdmin)
