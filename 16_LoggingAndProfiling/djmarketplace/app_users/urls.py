from django.urls import path
from app_users.views import LoginView, LogoutView, register_view, AccountView, AccountTopUpView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/', AccountView.as_view(), name='account'),
    path('account_topup/', AccountTopUpView.as_view(), name='account_topup'),
]