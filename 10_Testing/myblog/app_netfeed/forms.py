from django import forms
from app_netfeed.models import Feeds, Images


class CreateFeedForm(forms.ModelForm):

    class Meta:
        model = Feeds
        fields = ['title', 'text']


class CreateFeedImageForm(forms.Form):
    file = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))


class CreateFileFeedForm(forms.Form):
    feed_file = forms.FileField()