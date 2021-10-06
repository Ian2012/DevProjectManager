from django.urls import path

from .views import CommentListCreate, TicketListCreate, TicketRetrieveUpdateDestroy

app_name = 'core_api'

urlpatterns = [
    path('tickets', TicketListCreate.as_view(), name='create_ticket'),
    path('ticket/<int:pk>', TicketRetrieveUpdateDestroy.as_view(), name='create_update'),
    path('ticket/<int:pk>/comments', CommentListCreate.as_view(), name='create_comment'),
]
