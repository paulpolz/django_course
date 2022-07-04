from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from app_users.forms import RegisterForm
from django.contrib.auth.models import User
from app_users.models import Profile


# Форма регистрации
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            birth_date = form.cleaned_data.get('birth_date')
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            Profile.objects.create(
                user_login=user,
                birth_date=birth_date,
                city=city,
                phone=phone
            )

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})


# Форма авторизации
class LoginView(LoginView):
    template_name = 'app_users/login.html'


# Выход из под учетной записи
class LogoutView(LogoutView):
    template_name = 'app_users/logout.html'