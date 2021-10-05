from rest_framework import serializers

from apps.core.models import Ticket, TicketComment


class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    state_display = serializers.CharField(source='get_state_display', read_only=True)
    comments = TicketCommentSerializer(many=True, read_only=True)
    edit = serializers.BooleanField(default=False)

    class Meta:
        model = Ticket
        fields = '__all__'
