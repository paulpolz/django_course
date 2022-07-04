from django.http import response
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from news_app.models import *
from users_app.models import Profile
from news_app.forms import *
from django.urls import reverse
from datetime import datetime


# class NewsListView(ListView):
#     model = News
#     template_name = 'news_app/news_list.html'
#     context_object_name = 'news_list'
#     categories = Category.objects.all()

#     def get(self, request, *args, **kwargs):
#         is_moderator = request.user.groups.filter(name='Moderator').exists()
#         if is_moderator:
#             queryset = News.objects.order_by('-date_updated')[:10]
#         else:
#             queryset = News.objects.filter(is_active = True).order_by('-date_updated')[:10]
#         return render(request, 'news_app/news_list.html', context={'categories': self.categories, 'news_list': queryset, 'is_moderator': is_moderator})

#     def post(self, request):
#         is_moderator = request.user.groups.filter(name='Moderator').exists()

#         # Список всех возможных категорий ввода для проверки
#         input_names = []
#         for category in self.categories:
#             input_names.append(str(category) + '_choice')

#         # Запись значений категорий из формы
#         category_id_list = []
#         for name in input_names:
#             try:
#                 category_choice = request.POST[name]
#                 # Переход от названия категории к id для фильтрации
#                 category_id = Category.objects.get(name = category_choice).id
#                 category_id_list.append(category_id)
#             except:
#                 pass
        
#         # Если в форме не были выбраны категории, то берем все категории
#         if not category_id_list:
#                 for category in self.categories:
#                     category_id = Category.objects.get(name = category).id
#                     category_id_list.append(category_id)
        
#         # Запись даты из формы
#         try:
#             date_choice = datetime.strptime(request.POST['date_choice'], '%Y-%m-%d')

#             if is_moderator:
#                 queryset = News.objects.filter(category_id__in = category_id_list, date_created__year = date_choice.year, date_created__month = date_choice.month, date_created__day = date_choice.day).order_by('-date_updated')[:10]
#             else:
#                 queryset = News.objects.filter(is_active = True, category_id__in = category_id_list, date_created__year = date_choice.year, date_created__month = date_choice.month, date_created__day = date_choice.day).order_by('-date_updated')[:10]
#         except:
#             # Если в форме не была введена дата, то фильтруем новости без нее
#             if is_moderator:
#                 queryset = News.objects.filter(category_id__in = category_id_list).order_by('-date_updated')[:10]
#             else:
#                 queryset = News.objects.filter(is_active = True, category_id__in = category_id_list).order_by('-date_updated')[:10]
        
#         return render(request, 'news_app/news_list.html', context={'categories': self.categories, 'news_list': queryset, 'is_moderator': is_moderator})


class NewsListView(View):
    categories = Category.objects.all()

    def get(self, request):
        is_moderator = request.user.groups.filter(name='Moderator').exists()

        # модератор получает доступ ко всем новостям
        if is_moderator:
            qs = News.objects.all()
        else:
            qs = News.objects.filter(is_active = True)
        
        # Если выбрана категория, фильтруем по новсти
        if request.GET.get('category'):
            qs = qs.filter(category = Category.objects.get(name = request.GET.get('category')))

        # Финальная сортировка
        qs = qs.order_by('-date_updated')[:10]

        return render(request, 'news_app/news_list.html', context={'categories': self.categories, 'news_list': qs, 'is_moderator': is_moderator})



class NewsDetailView(DetailView):
    model = News
    template_name = 'news_app/news_detail.html'
    context_object_name = 'news_detail'

    def get_context_data(self,  **kwargs):
        news_object = super().get_object()
        context = super(NewsDetailView, self).get_context_data() 
        context['comment_form'] = NewCommentForm()
        context['comments'] = Comment.objects.filter(news_item_id=news_object.id)
        context['comments_count'] = Comment.objects.filter(news_item_id=news_object.id).count()
        context['category'] = Category.objects.get(name=news_object.category)
        context['date_created'] = News.objects.get(id=news_object.id).date_created.date()

        #  Изменять новость имеет право только ее создатель или модератор
        if self.request.user.id == News.objects.get(id=news_object.id).author_id or self.request.user.has_perm('news_app.change_news'):
            context['has_perm_to_change'] = True

        news_object.views_count = news_object.views_count + 1
        news_object.save()
    
        return context 

    def post(self, request, pk):

        # Если юзер аутентифицирован, то в качестве Автора коммента используем его ник
        if request.user.is_authenticated:
            comment_object = super().get_object()
            comment = NewCommentFormAuth(request.POST, instance=comment_object)

            if comment.is_valid():
                comment.cleaned_data['news_item_id'] = comment_object.id
                comment.cleaned_data['user_id'] = request.user.id

                Comment.objects.create(**comment.cleaned_data)

                return HttpResponseRedirect(reverse('news_detail', args=[str(pk)]))

            return render(request, 'news_app/news_detail.html', context={'comment': comment})
        
        # Если юзер не аутентифицирован, то добавляем в базу введенный им ник и используем его с приставкой Аноним
        else:
            comment = NewCommentForm(request.POST)
            
            if comment.is_valid():
                comment.cleaned_data['news_item_id'] = str(pk)
                Comment.objects.create(**comment.cleaned_data)
                return HttpResponseRedirect(reverse('news_detail', args=[str(pk)]))

            return render(request, 'news_app/news_detail.html', context={'comment': comment})


class CreateNewsItemView(View):

    def get(self, request):
        # Только Модератор может активировать новость в моммент ее создания
        is_moderator = request.user.groups.filter(name='Moderator').exists()
        
        news_item = CreateNewsItemForm()
        is_verified = request.user.has_perm('news_app.add_news')
        return render(request, 'news_app/create_news_item.html', context={'news_item': news_item, 'is_verified': is_verified, 'is_moderator': is_moderator})

    def post(self, request):
        news_item = CreateNewsItemForm(request.POST)
        if news_item.is_valid():
            news_item.cleaned_data['author_id'] = request.user.id
            news_item.cleaned_data['is_active'] = False
            News.objects.create(**news_item.cleaned_data)
            return HttpResponseRedirect('/news_list')

        profile = Profile.objects.get(user_id = request.user.id)
        profile.news_count = News.objects.filter(author_id = request.user.id).count()
        profile.save()
        
        return render(request, 'news_app/create_news_item.html', context={'news_item': news_item})


class UpdateNewsItemView(View):
    def get(self, request, pk):
        is_moderator = request.user.groups.filter(name='Moderator').exists()
        # Пользователь должен быть автором новости, которую он хочет поменять 
        # ИЛИ у него есть права на изменение новостей
        if not request.user.has_perm('news_app.change_news'):
            if not request.user.id == News.objects.get(id=pk).author_id:
                raise PermissionError
        news_item_id = News.objects.get(id=pk)
        news_item = CreateNewsItemForm(instance=news_item_id)
        return render(request, 'news_app/update_news_item.html', context={'news_item': news_item, 'pk': pk, 'is_moderator': is_moderator})

    def post(self, request, pk):
        news_item_id = News.objects.get(id=pk)
        news_item = CreateNewsItemForm(request.POST, instance=news_item_id)
        
        if news_item.is_valid():
            news_item.save()
            return HttpResponseRedirect(reverse('news_list'))

        return render(request, 'news_app/update_news_item.html', context={'news_item': news_item, 'pk': pk})

