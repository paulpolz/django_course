from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from app_users.forms import RegisterForm
from django.contrib.auth.models import User
from app_users.models import Profile
from django.views import View
from app_storage.models import Cart, Order
from app_loyalty.models import Balance
from app_users.forms import BonusBalanceUpdateForm


# Форма регистрации
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            birth_date = form.cleaned_data.get('birth_date')
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            # Создание профиля пользователя
            Profile.objects.create(
                user_login=user,
                birth_date=birth_date,
                city=city,
                phone=phone
            )
            # Создание бонусного счета
            Balance.objects.create(
                user=user
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


class AccountView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        orders_list = Order.objects.filter(user_id=user).prefetch_related('article').select_related('status').all()
        cart_list = Cart.objects.filter(user_id=user).select_related('article').all()
        bonus_account = Balance.objects.get(user_id=user)

        query_params = {
            'cart_list': cart_list,
            'orders_list': orders_list,
            'bonus_account': bonus_account,
        }

        return render(request, 'app_users/account.html', query_params)
    

class AccountTopUpView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        bonus_account = Balance.objects.get(user_id=user)
        bonus_balance_update_form = BonusBalanceUpdateForm()

        query_params = {
            'bonus_account': bonus_account,
            'bonus_balance_update_form': bonus_balance_update_form,
        }

        return render(request, 'app_users/account_topup.html', query_params)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        bonus_account = Balance.objects.get(user_id=user)
        bonus_balance_update_form = BonusBalanceUpdateForm(request.POST)

        if bonus_balance_update_form.is_valid():
            bonus_account.balance = bonus_account.balance + bonus_balance_update_form.cleaned_data['balance']
            bonus_account.save()

        return HttpResponseRedirect('/account')