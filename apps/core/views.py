from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from apps.core.forms import UserRegistrationForm
from apps.core.models import Project


class Home(LoginRequiredMixin, generic.ListView):
    template_name = 'core/home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(company=self.request.user.company)


class Login(views.LoginView):
    template_name = 'core/login.html'


class Logout(LoginRequiredMixin, views.LogoutView):
    next_page = '/login'


class Signup(generic.CreateView):
    template_name = 'core/signup.html'
    success_url = '/'
    form_class = UserRegistrationForm


class ProjectDetail(generic.DetailView):
    template_name = 'core/project_detail.html'
    context_object_name = 'project'

    def get_object(self, queryset=None):
        return Project.objects.get(id=self.kwargs['pk'])
