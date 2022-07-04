from django.db import models
import uuid
from django.urls import reverse


class PropertyType(models.Model):
    property_type_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    property_type_lv1 = models.CharField(max_length=50, verbose_name='Type of property level 1')
    property_type_lv2 = models.CharField(max_length=50, verbose_name='Type of property level 2')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property_type_lv1

    class Meta:
        verbose_name = ('Property Type')
        verbose_name_plural = ('Property Types')


class PropertyParameter(models.Model):
    parameter_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    parameter_name = models.CharField(max_length=50, verbose_name='Parameter name')
    parameter_value = models.CharField(max_length=50, verbose_name='Parameter value')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.parameter_name + ': ' + self.parameter_value

    class Meta:
        verbose_name = ('Property Parameter')
        verbose_name_plural = ('Property Parameters')


class Property(models.Model):
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, verbose_name='Property name')
    description = models.TextField(verbose_name='Property description')
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    parameter = models.ManyToManyField(PropertyParameter)
    price = models.FloatField(verbose_name='Price')
    is_published = models.BooleanField(verbose_name='Is published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Property')
        verbose_name_plural = ('Properties')