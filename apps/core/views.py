from django.contrib.auth import views
from django.views import generic

from apps.core.forms import UserRegistrationForm


class Home(generic.TemplateView):
    template_name = 'core/home.html'


class Login(views.LoginView):
    template_name = 'core/login.html'


class Logout(views.LogoutView):
    next_page = '/login'


class Signup(generic.CreateView):
    template_name = 'core/signup.html'
    success_url = '/'
    form_class = UserRegistrationForm
