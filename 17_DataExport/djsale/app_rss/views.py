from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app_rss.models import News


class NewsList(ListView):
    model = News
    template_name = 'app_rss/news.html'
    context_object_name = 'news'
    queryset = News.objects.filter(is_published=True).all()


class NewsDetail(DetailView):
    model = News
    template_name = 'app_rss/news_detail.html'
    context_object_name = 'article'