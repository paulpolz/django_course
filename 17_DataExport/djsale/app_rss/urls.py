import imp
from django.urls import path
from app_rss.views import NewsList, NewsDetail
from app_rss.feeds import LatestNews

urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('news/article/<pk>', NewsDetail.as_view(), name='article'),
    path('news/feed', LatestNews()),
]