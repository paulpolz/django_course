from django import forms
from app_news.models import News, Comment


class CreateNewsItemForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'author', 'category', 'text', 'is_active']


class NewCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user', 'comment']
