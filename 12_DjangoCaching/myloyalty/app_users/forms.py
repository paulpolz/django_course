from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text=_('First Name'))
    last_name = forms.CharField(max_length=50, required=True, help_text=_('Second Name'))
    birth_date = forms.DateField(help_text=_('Date of Birth'))
    email = forms.EmailField(max_length=256, help_text=_('Email'))
    city = forms.CharField(max_length = 50, required=False, help_text=_('City'))
    phone = forms.CharField(max_length = 36, required=True, help_text=_('Phone Number'), widget=forms.TextInput(attrs={'type':'number'}))


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']