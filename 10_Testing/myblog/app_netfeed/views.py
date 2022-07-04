from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import request
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from app_netfeed.models import Feeds, Images
from app_netfeed.forms import CreateFeedForm, CreateFeedImageForm, CreateFileFeedForm
from csv import reader, excel_tab


class FeedsListView(ListView):
    model = Feeds
    template_name = 'netfeed/feed_list.html'
    context_object_name = 'feeds_list'
    queryset = Feeds.objects.order_by('-date_updated').all()


class FeedsDetailView(DetailView):
    model = Feeds
    template_name = 'netfeed/feed_detail.html'
    context_object_name = 'feed_detail'

    def get_context_data(self,  **kwargs):
        feeds_object = super().get_object()
        context = super(FeedsDetailView, self).get_context_data() 
        context['images'] = Images.objects.filter(feed_id=feeds_object.id)

        return context 


class CreateFeedView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionError('You are not logged in')
        feed = CreateFeedForm()
        image = CreateFeedImageForm()
        return render(request, 'netfeed/feed_create.html', context={'feed': feed, 'image': image})

    def post(self, request):
        feed = CreateFeedForm(request.POST)
        image = CreateFeedImageForm(request.POST, request.FILES)

        if feed.is_valid() and image.is_valid():
            title = feed.cleaned_data.get('title')
            author_id = request.user.id
            text = feed.cleaned_data.get('text')
            Feeds.objects.create(
                title=title,
                author_id=author_id,
                text=text
            )

            try:
                files = request.FILES.getlist('file')
                for file in files:
                    Images.objects.create(
                        feed_id=Feeds.objects.latest('id').id,
                        file=file
                    )
            except:
                pass

            return HttpResponseRedirect('/feeds/list')

        return render(request, 'netfeed/feed_create.html', context={'feed': feed, 'image': image})


class CreateFileFeedView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionError('You are not logged in')
        feed_file = CreateFileFeedForm()
        return render(request, 'netfeed/feed_create_file.html', context={'feed_file': feed_file})

    def post(self, request):
        feed_file = CreateFileFeedForm(request.POST, request.FILES)

        if feed_file.is_valid():

            feed_file_cleaned = feed_file.cleaned_data['feed_file'].read().decode('utf-8').split('\n')

            csv_reader = reader(feed_file_cleaned, delimiter=";", dialect=excel_tab)
            for row in csv_reader:
                title = row[0]
                author_id = request.user.id
                text = row[1]
                Feeds.objects.create(
                    title=title,
                    author_id=author_id,
                    text=text
                )
            return HttpResponseRedirect('/feeds/list')

        return render(request, 'netfeed/feed_create_file.html', context={'feed_file': feed_file})
