from django import forms
from app_news.models import News, Comments


class CreateNewsItemForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class NewCommentForm(forms.ModelForm):

    class Meta:
        model = Comments
<<<<<<< HEAD
        fields = ['user_name', 'comment']
=======
        fields = ['comment']  # убрал поле ВК на новость, чтобы оно не отображалось в форме
>>>>>>> 58f34e07b07a5a35909f79ea45e42ba0c4bdb089
