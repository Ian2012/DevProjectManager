from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Project, Ticket, User, UserStory


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'company', 'password1', 'password2')


class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = ('description', 'project')
        widgets = {'project': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(id=kwargs['initial']['project'])


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('description', 'user_story')
        widgets = {'user_story': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['user_story'].queryset = UserStory.objects.filter(id=kwargs['initial']['user_story'])
