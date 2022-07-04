from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth import authenticate, login
from app_users.forms import RegisterForm, ProfileEditForm, ProfileInitEditForm
from django.contrib.auth.models import User
from app_users.models import Profile


# Форма регистрации
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            about_me = form.cleaned_data.get('about_me')
            avatar = request.FILES.get('avatar')
            print('111111111111111111111111111111', avatar)
            Profile.objects.create(
                user_login=user,
                city=city,
                phone=phone,
                about_me=about_me,
                avatar=avatar
            )

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Форма авторизации
class LoginView(LoginView):
    template_name = 'users/login.html'


# Выход из под учетной записи
class LogoutView(LogoutView):
    template_name = 'users/logout.html'


# Профиль юзера
class UsersProfile(DetailView):

    model = Profile
    template_name = 'users/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        if not self.request.user.id == User.objects.get(id=self.kwargs['pk']).id:
            raise PermissionError
        context = super(UsersProfile, self).get_context_data(**kwargs)
        context['init_profile'] = User.objects.get(id=self.kwargs['pk'])
        return context


# Изменить профиль юзера
class UsersProfileEdit(View):
    def get(self, request, *args, **kwargs):
        if not request.user.id == User.objects.get(id=self.kwargs['pk']).id:
            raise PermissionError
        instance_init_id = User.objects.get(id=request.user.id)
        instance_id = Profile.objects.get(user_login_id=request.user.id)

        edit_init_form = ProfileInitEditForm(instance=instance_init_id)
        edit_form = ProfileEditForm(instance=instance_id)

        return render(request, 'users/profile_edit.html', context={'edit_form': edit_form, 'edit_init_form': edit_init_form, 'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        instance_init_id = User.objects.get(id=request.user.id)
        instance_id = Profile.objects.get(user_login_id=request.user.id)

        edit_init_form = ProfileInitEditForm(request.POST, instance=instance_init_id)
        edit_form = ProfileEditForm(request.POST, instance=instance_id)

        if edit_form.is_valid() and edit_init_form.is_valid():
            edit_init_form.save()
            edit_form.save()
            return HttpResponseRedirect('/users/profile/'+str(request.user.id))

        return render(request, 'users/profile_edit.html', context={'edit_form': edit_form, 'edit_init_form': edit_init_form, 'pk': self.kwargs['pk']})