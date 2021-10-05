from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Project, User, UserStory


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'company', 'password1', 'password2')


class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = ('description', 'project')

    def __init__(self, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(id=kwargs['initial']['project'])
