from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse
from app_rss.models import News


class LatestNews(Feed):
    title = 'Новости'
    link = '/sitenews/'
    description = 'Самые свежие новости.'

    def items(self) -> QuerySet:
        return News.objects.filter(is_published=True).order_by('-updated_at')[:10]

    def item_title(self, item: News) -> str:
        return item.title

    def item_description(self, item: News) -> str:
        return item.text

    def item_link(self, item: News) -> str:
        return reverse('article', args=[item.pk])