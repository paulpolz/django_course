from django.urls import path
from users_app.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<int:pk>/', UsersProfile.as_view(), name='users_account'),
]
