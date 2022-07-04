from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок новости')
    text = models.TextField(verbose_name='Содержание')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(verbose_name='Флаг активности')

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_name = models.CharField(max_length=20)
    comment = models.TextField(max_length=250)
    news_item = models.ForeignKey('News', default=None, related_name='news', on_delete=models.CASCADE)