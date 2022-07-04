from django.urls import path
from app_estate.views import PropertyList, About, Contacts, get_properties_in_custom_format

urlpatterns = [
    path('properties/', PropertyList.as_view(), name='properties'),
    path('about/', About.as_view(), name='about'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('properties/get', get_properties_in_custom_format, name='properties_get'),
]