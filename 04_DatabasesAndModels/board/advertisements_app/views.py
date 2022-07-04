from django.views.generic import ListView, DetailView
from advertisements_app.models import Advertisements
from datetime import datetime
from pycbrf.toolbox import ExchangeRates


class AdvertisementsList(ListView):
    model = Advertisements
    template_name = 'advertisements_app/advertisements_list.html'
    context_object_name = 'advertisements_list'
    queryset = Advertisements.objects.all()[:10]

class AdvertisementDetail(DetailView):  # TODO Определение класса отделяется от остального кода двумя пустыми строками
    model = Advertisements
    template_name = 'advertisements_app/advertisement_detail.html'
    context_object_name = 'advertisement_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usd_currency = float(ExchangeRates(datetime.now().date().strftime("%Y-%m-%d"))['USD'].value)
        price_in_rub = Advertisements.objects.get(id=self.kwargs['pk']).price
        context['price_in_usd'] = round(price_in_rub / usd_currency, 2)
        return context   # TODO В конце модуля оставляйте пустую строку