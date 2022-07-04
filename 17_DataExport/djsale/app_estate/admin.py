from django.contrib import admin
from app_estate.models import PropertyType, PropertyParameter, Property


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ['property_type_id', 'property_type_lv1', 'property_type_lv2', 'updated_at']


@admin.register(PropertyParameter)
class PropertyParameterAdmin(admin.ModelAdmin):
    list_display = ['parameter_id', 'parameter_name', 'parameter_value', 'updated_at']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price', 'is_published', 'updated_at']
