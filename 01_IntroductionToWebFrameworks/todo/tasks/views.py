from django.http import HttpResponse

from django.views import View

import random


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        li_list = [
            '<li>Установить python</li>',
            '<li>Установить django</li>',
            '<li>Запустить сервер</li>',
            '<li>Порадоваться результату</li>',
            '<li>Продолжать улучшать приложение</li>'
        ]

        random.shuffle(li_list)
        
        http = ['<ul>'] + li_list + ['<ul>']
        
        return HttpResponse(http)
