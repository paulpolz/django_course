from django.urls import path
from .import views

urlpatterns = [
	path('', views.advertisement_list, name='advertisement_list'),
	path('advertisement_01/', views.advertisement_detail_01, name='advertisement_detail_01'),
	path('advertisement_02/', views.advertisement_detail_02, name='advertisement_detail_02'),
	path('advertisement_03/', views.advertisement_detail_03, name='advertisement_detail_03'),
	path('advertisement_04/', views.advertisement_detail_04, name='advertisement_detail_04'),
	path('advertisement_05/', views.advertisement_detail_05, name='advertisement_detail_05')
]