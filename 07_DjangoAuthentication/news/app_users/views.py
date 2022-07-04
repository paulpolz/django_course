from django.contrib.auth.views import LoginView, LogoutView


class LoginView(LoginView):
    template_name = 'app_users/login.html'
    

class LogoutView(LogoutView):
    template_name = 'app_users/logout.html'
    # next_page = '/'