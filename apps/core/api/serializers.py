from rest_framework import serializers

from apps.core.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='get_state_display')

    class Meta:
        model = Ticket
        fields = '__all__'
