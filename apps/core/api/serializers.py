from rest_framework import serializers

from apps.core.models import Ticket, TicketComment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class TicketCommentListSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = TicketComment
        fields = '__all__'


class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketComment
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    state_display = serializers.CharField(source='get_state_display', read_only=True)
    comments = TicketCommentListSerializer(many=True, read_only=True)
    edit = serializers.BooleanField(default=False)
    comment = serializers.BooleanField(default=False)

    class Meta:
        model = Ticket
        fields = '__all__'
