from django.db import models
from django.utils.translation import gettext_lazy as _


class Feeds(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('Заголовок поста'))
    author = models.ForeignKey('app_users.Profile', verbose_name=_('Автор поста'), on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_('Основной текст'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('новости')
        verbose_name = _('новость')


class Images(models.Model):
    feed = models.ForeignKey('Feeds', default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to='netfeed/images', verbose_name=('Иллюстрация'))