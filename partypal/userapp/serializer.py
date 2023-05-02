from rest_framework.serializers import ModelSerializer
from .models import User, Event, Guest, Host, Venue

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'is_organizer', 'is_guest')

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'location', 'description', 'host', 'guests', 'created_at')

