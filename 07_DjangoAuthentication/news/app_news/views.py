from django.http.response import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from app_news.forms import *
from app_news.models import *
from app_news.static.scripts import news_parser
from django.urls import reverse


class NewsListView(ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.filter(is_active = True).order_by('-date_updated')[:10]
    
    def post(self, request):
        
        # Парсинг данных с сайта
        url = 'https://vc.ru'
        news_link_list = news_parser.get_links_from_main(url)
        headers_list, authors_list, content_blocks = news_parser.get_content_from_news_pages(news_link_list)

        # Загрузка полученных данных в БД 
        for i in range(len(headers_list)):
        #     # Поиск автора или создание нового автора
        #     if User.objects.filter(user_nick = authors_list[i]).count() == 0:
        #         User.objects.create(user_nick = authors_list[i], is_author = 1)
        #     new_author_id = User.objects.get(user_nick=authors_list[i]).id

            News.objects.create(title = headers_list[i], author_id=request.user.id , category_id=1, text = content_blocks[i], is_active = 1)

        return render(request, 'app_news/news_list.html', context={'news_list': self.queryset})


class NewsDetailView(DetailView):
    model = News
    template_name = 'app_news/news_detail.html'
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
        comment_object = super().get_object()
        context = super(NewsDetailView, self).get_context_data() 
        context['comment_form'] = NewCommentForm()
        context['comments'] = Comment.objects.filter(news_item_id=comment_object.id)
        context['comments_count'] = Comment.objects.filter(news_item_id=comment_object.id).count()
        context['category'] = Category.objects.get(name=comment_object.category)
        context['date_created'] = News.objects.get(id=comment_object.id).date_created.date()

        comment_object.views_count = comment_object.views_count + 1
        comment_object.save()
    
        return context 

    def post(self, request, pk):

        # Если юзер аутентифицирован, то в качестве Автора коммента используем его ник
        if request.user.is_authenticated:
            comment_object = super().get_object()
            comment = NewCommentFormAuth(request.POST, instance=comment_object)
            print(request.user.id)
            if comment.is_valid():
                comment.cleaned_data['news_item_id'] = comment_object.id
                comment.cleaned_data['user_id'] = request.user.id

                Comment.objects.create(**comment.cleaned_data)

                return HttpResponseRedirect(reverse('news_detail', args=[str(pk)]))

            return render(request, 'app_news/news_detail.html', context={'comment': comment})
        
        # Если юзер не аутентифицирован, то добавляем в базу введенный им ник и используем его с приставкой Аноним
        else:
            comment = NewCommentForm(request.POST)
            
            if comment.is_valid():
                comment.cleaned_data['news_item_id'] = str(pk)
                Comment.objects.create(**comment.cleaned_data)
                return HttpResponseRedirect(reverse('news_detail', args=[str(pk)]))

            return render(request, 'app_news/news_detail.html', context={'comment': comment})


class CreateNewsItemView(View):

    def get(self, request):
        # Если пользователь авторизован, то у него есть доступ создавать новости
        if request.user.is_authenticated:
            news_item = CreateNewsItemForm()
            return render(request, 'app_news/create_news_item.html', context={'news_item': news_item})
        # Если нет, то ему надо сачала авторизоваться
        else:
            return HttpResponseRedirect(reverse('login'))

    def post(self, request):
        news_item = CreateNewsItemForm(request.POST)

        if news_item.is_valid():
            news_item.cleaned_data['author_id'] = request.user.id
            News.objects.create(**news_item.cleaned_data)
            return HttpResponseRedirect(reverse('news_list'))  # TODO а вы проверяли работу проекта, ведь тут проект
            # падает? Почему-то в urls.py имя роутинга для страницы списка новостей - news_item

        return render(request, 'app_news/create_news_item.html', context={'news_item': news_item})


class UpdateNewsItemView(View):

    def get(self, request, profile_id):
        # Если пользователь авторизован, то у него есть доступ изменять новости
        if request.user.is_authenticated:
            news_item_id = News.objects.get(id=profile_id)
            news_item = CreateNewsItemForm(instance=news_item_id)
            return render(request, 'app_news/update_news_item.html', context={'news_item': news_item, 'profile_id': profile_id})
        # Если нет, то ему надо сачала авторизоваться
        else:
            return HttpResponseRedirect(reverse('login'))

    def post(self, request, profile_id):
        news_item_id = News.objects.get(id=profile_id)
        news_item = CreateNewsItemForm(request.POST, instance=news_item_id)

        if news_item.is_valid():
            news_item.save()
            return HttpResponseRedirect(reverse('news_list'))

        return render(request, 'app_news/update_news_item.html', context={'news_item': news_item, 'profile_id': profile_id})

