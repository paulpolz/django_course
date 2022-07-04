from django import forms
from django.db.models import fields
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users_app.models import Profile


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Имя')
    last_name = forms.CharField(max_length=50, required=True, help_text='Фамилия')
    email = forms.EmailField(max_length=256, help_text='Email')
    city = forms.CharField(max_length = 50, required=False, help_text='Город')
    phone = forms.CharField(max_length = 36, required=True, help_text='Номер телефона', widget=forms.TextInput(attrs={'type':'number'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone', 'city', 'is_verified', 'is_moderator']
