from django import forms
from news_app.models import News, Comment


class CreateNewsItemForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'category', 'text', 'is_active']

    
class NewCommentForm(forms.Form):
    nickname = forms.CharField(max_length=25)
    comment = forms.CharField(widget=forms.Textarea)


class NewCommentFormAuth(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']