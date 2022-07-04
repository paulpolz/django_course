from django.urls import path
from app_storage.views import ShowcaseListView, ShowCaseDetailView, CartView

urlpatterns = [
    path('showcase/', ShowcaseListView.as_view(), name='showcase'),
    path('good/<uuid:pk>/', ShowCaseDetailView.as_view(), name='good'),
    path('cart/', CartView.as_view(), name='cart'),
]