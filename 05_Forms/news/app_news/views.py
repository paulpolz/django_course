from django.http.response import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from app_news.forms import *
from app_news.models import *


class NewsListView(ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.filter(is_active = True).order_by('-date_updated')[:10]


class NewsDetailView(DetailView):
    model = News
    template_name = 'app_news/news_detail.html'
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
<<<<<<< HEAD
        comment_object = super().get_object()
        context = super(NewsDetailView, self).get_context_data() 
        context['comment_form'] = NewCommentForm()
        context['comments'] = Comments.objects.filter(news_item_id=comment_object.id)
        context['comments_count'] = Comments.objects.filter(news_item_id=comment_object.id).count()
        return context 

    def post(self, request, pk):
        comment_object = super().get_object()
        comment = NewCommentForm(request.POST, instance=comment_object)

        if comment.is_valid():
            comment.cleaned_data['news_item_id'] = comment_object.id
=======
        comment_id = super().get_object()
        context = super(NewsDetailView, self).get_context_data()
        context['comment_form'] = NewCommentForm()
        context['comments'] = Comments.objects.filter(news_item_id=comment_id.id)
        context['comments_count'] = Comments.objects.filter(news_item_id=comment_id.id).count()
        return context

    def post(self, request, pk):
        comment_id = super().get_object()  # TODO уберите id из имени переменной, ведь это сам объект записи целиком,
                                           #  а не одно поле
        comment = NewCommentForm(request.POST)

        if comment.is_valid():
            comment.cleaned_data['news_item_id'] = comment_id.id  # заполняем поле без участия пользователя
>>>>>>> 58f34e07b07a5a35909f79ea45e42ba0c4bdb089
            Comments.objects.create(**comment.cleaned_data)
            return HttpResponseRedirect('/news_detail/' + str(pk))

        return render(request, 'app_news/news_detail.html', context={'comment': comment})


class CreateNewsItemView(View):

    def get(self, request):
        news_item = CreateNewsItemForm()
        return render(request, 'app_news/create_news_item.html', context={'news_item': news_item})

    def post(self, request):
        news_item = CreateNewsItemForm(request.POST)

        if news_item.is_valid():
            News.objects.create(**news_item.cleaned_data)
            return HttpResponseRedirect('/news_list')

        return render(request, 'app_news/create_news_item.html', context={'news_item': news_item})


class UpdateNewsItemView(View):

    def get(self, request, profile_id):
        news_item_id = News.objects.get(id=profile_id)
        news_item = CreateNewsItemForm(instance=news_item_id)
        return render(request, 'app_news/update_news_item.html', context={'news_item': news_item, 'profile_id': profile_id})

    def post(self, request, profile_id):
        news_item_id = News.objects.get(id=profile_id)
        news_item = CreateNewsItemForm(request.POST, instance=news_item_id)

        if news_item.is_valid():
            news_item.save()
            return HttpResponseRedirect('/news_list')

        return render(request, 'app_news/update_news_item.html', context={'news_item': news_item, 'profile_id': profile_id})

