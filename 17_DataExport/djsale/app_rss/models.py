from django.db import models
import uuid
from django.urls import reverse


class News(models.Model):
    news_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=55, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    is_published = models.BooleanField(verbose_name='Is published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("article", args=[str(self.news_id)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('News')
        verbose_name_plural = ('News')