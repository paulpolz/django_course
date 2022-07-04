from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic import TemplateView


class Main(TemplateView):
    template_name = 'advertisements/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = [
            'Репетиторы',
            'Мастера по ремонту',
            'Фрилансеры',
            'Артисты',
            'Юристы',
            'Домашний персонал'
        ]
        context['regions'] = [
            'Москва',
            'Московская область',
            'Санкт-Петербург',
            'Нижний Новгород',
            'Казань',
            'Волгоград',
            'Екатеринбург'
        ]
        return context


class Advertisements(View):
    advertisement_list = [
        'Сантехника',
        'Уборка',
        'Установка кондиционеров',
        'Массаж',
        'Выгул собак',
        'Преподавание'
    ]
    counter = 0

    def get(self, request):
        return render(request, 'advertisements/advertisements.html', {'advertisements': self.advertisement_list})

    def post(self, request):
        status_message = 'Запрос на создание новой записи успешно выполнен'
        print(status_message)

        Advertisements.counter += 1
        print(Advertisements.counter)

        return render(request, 'advertisements/advertisements.html', {'advertisements': self.advertisement_list, 'counter': Advertisements.counter})


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'Московская обл., г. Долгопрудный'
        context['phone'] = '+7(999)145-07-07'
        context['email'] = 'add_ads@inbox.com'
        
        return context


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['org_name'] = 'Add Advertisements'
        context['description'] = 'Сервис размещения объявлений в интернете'

        return context