from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .forms import CustomAuthenticationForm


class LoginView(auth_views.LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'minhashoras_apps/accounts/login.html'


class LogoutView(auth_views.LogoutView):
    template_name = 'accounts/logout.html'
    next_page = reverse_lazy('accounts:login')
