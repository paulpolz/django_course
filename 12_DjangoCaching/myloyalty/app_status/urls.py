from django.urls import path
from app_status.views import *

urlpatterns = [
    path('account/', PersonalAccount.as_view(), name='account'),
]