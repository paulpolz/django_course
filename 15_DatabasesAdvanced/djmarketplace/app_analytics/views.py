from django.shortcuts import render
from django.views import View
from app_storage.models import Order
from django.db.models import Sum
from app_analytics.forms import SalesReportDateFiterForm
from datetime import datetime
from django.utils.timezone import is_aware, make_aware


class SalesReportView(View):
    def get(self, request, *args, **kwargs):
        sales_top = Order.objects.select_related('article').values('article', 'article__good__good_name').annotate(sales=Sum('quantity')).order_by('-sales')[:100]
        sales_report_date_filter = SalesReportDateFiterForm()

        query_params = {
            'sales_top': sales_top,
            'sales_report_date_filter': sales_report_date_filter,
        }

        return render(request, 'app_analytics/sales_report.html', query_params)

    def post(self, request, *args, **kwargs):
        sales_report_date_filter = SalesReportDateFiterForm(request.POST)
        
        if sales_report_date_filter.is_valid():
            # Забираем даты для выгрузки отчета из формы
            start_date = sales_report_date_filter.cleaned_data['start_date']
            end_date = sales_report_date_filter.cleaned_data['end_date']

            # Проверяем таймзон, и если надо, то выставляем верный
            start_date = make_aware(datetime.combine(start_date, datetime.min.time()))
            end_date = make_aware(datetime.combine(end_date, datetime.min.time()))

        sales_top = Order.objects.filter(created_at__range=(start_date, end_date)).select_related('article').values('article', 'article__good__good_name').annotate(sales=Sum('quantity')).order_by('-sales')[:100]

        query_params = {
            'sales_top': sales_top,
            'sales_report_date_filter': sales_report_date_filter,
        }

        return render(request, 'app_analytics/sales_report.html', query_params)