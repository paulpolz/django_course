from django.contrib.sitemaps import Sitemap
from app_rss.models import News
from django.urls import reverse


class StaticSiteMap(Sitemap):
    change_freq = 'weekly'
    priority = 0.9

    def items(self):
        return ['about','contacts']

    def location(self, obj: News):
        return reverse(obj)


class NewsSiteMap(Sitemap):
    change_freq = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.filter(is_published=True).all()

    def lastmod(self, obj: News):
        return obj.updated_at