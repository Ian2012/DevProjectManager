from django.urls import path

from .views import TicketListCreate

app_name = 'core_api'

urlpatterns = [
    path('tickets', TicketListCreate.as_view(), name='create_ticket'),
]
