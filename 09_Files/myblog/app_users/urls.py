from django.urls import path
from app_users.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/<int:pk>/', UsersProfile.as_view(), name='profile'),
    path('profile/<int:pk>/edit', UsersProfileEdit.as_view(), name='profile_edit'),
]
