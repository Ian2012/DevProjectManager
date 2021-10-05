from rest_framework import serializers

from apps.core.models import Ticket, TicketComment


class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='get_state_display')
    comments = TicketCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'