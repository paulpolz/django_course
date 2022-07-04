from django.shortcuts import render
from django.utils.translation import templatize
from django.views.generic import ListView
from app_catalog.models import Store


class StoreListWiew(ListView):
    model = Store
    template_name = 'app_catalog/store_list.html'
    context_object_name = 'store_list'
    queryset = Store.objects.all()
