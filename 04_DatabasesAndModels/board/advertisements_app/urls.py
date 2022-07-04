from django.urls import path
from advertisements_app.views import *

urlpatterns = [
    path('advertisements/', AdvertisementsList.as_view(), name='advertisements'),
    path('advertisements/detail/<int:pk>', AdvertisementDetail.as_view(), name='advertisements_detail')
]
