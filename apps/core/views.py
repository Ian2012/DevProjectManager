from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic

from apps.core.forms import TicketForm, UserRegistrationForm, UserStoryForm
from apps.core.models import Project, UserStory


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


class UserStoryDetail(generic.FormView, generic.DetailView):
    template_name = 'core/user_story_detail.html'
    context_object_name = 'user_story'
    form_class = TicketForm

    def form_valid(self, form):
        form.save()
        return super(UserStoryDetail, self).form_valid(form)

    def get_object(self, queryset=None):
        return UserStory.objects.get(id=self.kwargs['story_pk'], project=self.kwargs['project_pk'])

    def get_initial(self):
        initial = super(UserStoryDetail, self).get_initial()
        initial = initial.copy()
        initial['user_story'] = self.kwargs['story_pk']
        return initial

    def get_success_url(self):
        return reverse('core:user_story_detail', kwargs={'project_pk': self.kwargs['project_pk'],
                                                         'story_pk': self.kwargs['story_pk']})


class UserStoryCreate(generic.CreateView):
    template_name = 'core/user_story_create.html'
    form_class = UserStoryForm

    def get_success_url(self):
        return reverse('core:user_story_detail', kwargs={'project_pk': self.kwargs['project_pk'],
                                                         'story_pk': self.object.id})

    def get_initial(self):
        initial = super(UserStoryCreate, self).get_initial()
        initial = initial.copy()
        initial['project'] = self.kwargs['project_pk']
        return initial
