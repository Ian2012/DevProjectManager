from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Project, Ticket, User, UserStory


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'company', 'password1', 'password2')


class UserStoryForm(forms.ModelForm):
    ticket = forms.CharField(max_length=64)

    class Meta:
        model = UserStory
        fields = ('description', 'project')
        widgets = {'project': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(UserStoryForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(id=kwargs['initial']['project'])

    def save(self, commit=True):
        story = super(UserStoryForm, self).save()
        Ticket.objects.create(user_story_id=story.id, description=self.cleaned_data['ticket']).save()
        return story


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('description', 'user_story')
        widgets = {'user_story': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['user_story'].queryset = UserStory.objects.filter(id=kwargs['initial']['user_story'])
        self.fields['description'].widget.attrs['class'] = 'bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500'
