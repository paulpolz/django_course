from django.urls import path
from app_catalog.views import *

urlpatterns = [
    path('stores/', StoreListWiew.as_view(), name='stores'),
]