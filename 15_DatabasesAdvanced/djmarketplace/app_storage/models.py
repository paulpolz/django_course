from django.db import models
from django.contrib.auth.models import User
import uuid


class Store(models.Model):
    store_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    store_name = models.CharField(max_length=200, verbose_name='Store Name')
    country = models.CharField(max_length=50, verbose_name='Country')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name

    class Meta:
        verbose_name_plural = ('Stores')
        verbose_name = ('Store')


class Good(models.Model):
    good_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    good_name = models.CharField(max_length=200, verbose_name='Good name')
    description = models.TextField(verbose_name='Good description')
    weight = models.FloatField(default=0, verbose_name='Weight')
    store = models.ManyToManyField(Store, verbose_name='Store Name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.good_name
    
    class Meta:
        verbose_name_plural = ('Goods')
        verbose_name = ('Good')


class Article(models.Model):
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='Store name')
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='Good name')
    price = models.FloatField(default=0, verbose_name='Price')
    stock = models.PositiveIntegerField(default=0, verbose_name='Stock')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.good) + ' from ' + str(self.store)

    class Meta:
        verbose_name_plural = ('Articles')
        verbose_name = ('Article')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = ('Carts')
        verbose_name = ('Cart')


class OrderStatus(models.Model):
    status_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status = models.CharField(max_length=100, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = ('OrderStatus')
        verbose_name = ('OrderStatuses')

def get_initial_order_status():
    registered_status = OrderStatus.objects.get(status='Registered')
    return registered_status


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, default=get_initial_order_status, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Quantity')
    price = models.FloatField(default=0, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = ('Order')
        verbose_name = ('Orders')