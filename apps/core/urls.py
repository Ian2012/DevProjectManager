from django.urls import path

from .views import Home, Login, Logout, ProjectDetail, Signup, UserStoryDetail

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # Auth
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', Logout.as_view(), name='logout'),
    # Projects
    path('project/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('project/<int:project_pk>/user_story/<int:story_pk>', UserStoryDetail.as_view(), name='user_story_detail'),

]
