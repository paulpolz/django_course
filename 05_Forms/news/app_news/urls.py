from django.urls import path
from app_news.views import *

urlpatterns = [
    path('news_list', NewsListView.as_view(), name='news_item'),
    path('news_detail/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news_list/create', CreateNewsItemView.as_view(), name='create_news_item'),
    path('news_detail/<int:profile_id>/update', UpdateNewsItemView.as_view(), name='update_news_item'),
]
