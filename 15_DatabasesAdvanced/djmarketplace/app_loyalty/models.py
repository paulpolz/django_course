from django.db import models
from django.contrib.auth.models import User
import uuid


class BalanceStatus(models.Model):
    status_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status = models.CharField(max_length=100, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = ('BalanceStatus')
        verbose_name = ('BalanceStatus')


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.ForeignKey(BalanceStatus, default=BalanceStatus.objects.get(status='Guest').status_id, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0, verbose_name='Balance')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)