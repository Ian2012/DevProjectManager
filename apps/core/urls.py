from django.urls import path

from .views import Home, Login, Logout, ProjectDetail, Signup

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # Auth
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', Logout.as_view(), name='logout'),
    # Projects
    path('project/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
]
