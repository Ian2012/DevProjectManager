from rest_framework import generics

from apps.core.models import Ticket, TicketComment
from .serializers import TicketCommentSerializer, TicketSerializer


class TicketListCreate(generics.ListCreateAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(user_story_id=self.request.query_params['user_story'])


class TicketRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = TicketCommentSerializer

    def get_queryset(self):
        return TicketComment.objects.filter(ticket_id=self.kwargs['pk'])
