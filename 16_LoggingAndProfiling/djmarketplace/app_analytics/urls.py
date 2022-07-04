from django.urls import path
from app_analytics.views import SalesReportView

urlpatterns = [
    path('sales_report/', SalesReportView.as_view(), name='sales_report'),
]