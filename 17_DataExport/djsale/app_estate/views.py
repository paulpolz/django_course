from re import template
from django.shortcuts import render
from django.views.generic import ListView
from app_estate.models import Property
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers


class PropertyList(ListView):
    model = Property
    template_name = 'app_estate/properties.html'
    context_object_name = 'properties'
    queryset = Property.objects.select_related('type').prefetch_related('parameter').all()


class About(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'app_estate/about.html', context={})


class Contacts(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'app_estate/contacts.html', context={})


def get_properties_in_custom_format(request):
    format = request.GET['format']
    if format not in ['xml', 'json', 'yaml']:
        return HttpResponseBadRequest
    data = serializers.serialize(format, Property.objects.all())
    return HttpResponse(data)