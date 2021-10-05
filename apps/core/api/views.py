from rest_framework import generics

from apps.core.models import Ticket
from .serializers import TicketSerializer


class TicketListCreate(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(user_story_id=self.request.query_params['user_story'])


class TicketRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
