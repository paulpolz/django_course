from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth import authenticate, login
from users_app.forms import RegisterForm, ProfileForm
from django.contrib.auth.models import User
from users_app.models import Profile


# Форма регистрации
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            Profile.objects.create(
                user=user,
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
    return render(request, 'users_app/register.html', {'form': form})


# Форма авторизации
class LoginView(LoginView):
    template_name = 'users_app/login.html'


# Выход из под учетной записи
class LogoutView(LogoutView):
    template_name = 'users_app/logout.html'


# Профиль юзера
class UsersProfile(View):
    def get(self, request, pk):
        is_moderator = request.user.groups.filter(name='Moderator').exists()
        # Пользователи (кроме модератора) могут просматривать только свой профиль
        if not self.request.user.groups.filter(name='Moderator').exists():
            if not self.request.user.id == pk:
                raise PermissionError
        
        profile_id = Profile.objects.get(user_id = pk)
        profile = ProfileForm(instance=profile_id)

        return render(request, 'users_app/profile.html', context={'profile': profile, 'username': profile_id.user, 'pk': pk, 'is_moderator': is_moderator})

    def post(self, request, pk):
        profile_id = Profile.objects.get(user_id = pk)
        profile = ProfileForm(request.POST, instance=profile_id)

        if profile.is_valid():
            profile.save()
        
        # Обновление прав пользователя
        if profile['is_verified'].value() == True:
            User.objects.get(id=pk).groups.add(2)
        if profile['is_moderator'].value() == True:
            User.objects.get(id=pk).groups.add(3)


        return render(request, 'users_app/profile.html', context={'profile': profile, 'username': profile_id.user, 'pk': pk})

