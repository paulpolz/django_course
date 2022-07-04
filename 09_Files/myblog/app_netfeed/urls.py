from django.urls import path
from app_netfeed.views import *

urlpatterns = [
    path('list/', FeedsListView.as_view(), name='list'),
    path('detail/<int:pk>', FeedsDetailView.as_view(), name='detail'),
    path('create/', CreateFeedView.as_view(), name='create'),
    path('create_file/', CreateFileFeedView.as_view(), name='create_file'),
]