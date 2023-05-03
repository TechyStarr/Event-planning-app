from rest_framework.serializers import ModelSerializer
from .models import User, Event, Guest, Host, Venue



class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'created_at')

# class GuestSerializer(ModelSerializer):
#     class Meta:
#         model = Guest
#         fields = ('id', 'name', 'email', 'phone', 'event')

# class HostSerializer(ModelSerializer):
#     class Meta:
#         model = Host
#         fields = ('id', 'name', 'email', 'phone', 'event')

# class VenueSerializer(ModelSerializer):
#     class Meta:
#         model = Venue
#         fields = ('id', 'name', 'address', 'event')

# Path: partypal\api\views.py