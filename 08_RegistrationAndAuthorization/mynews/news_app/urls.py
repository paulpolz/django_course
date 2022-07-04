from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from news_app.views import *

urlpatterns = [
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('news_detail/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news_list/create', CreateNewsItemView.as_view(), name='create_news_item'),
    path('news_detail/<int:pk>/update', UpdateNewsItemView.as_view(), name='update_news_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)